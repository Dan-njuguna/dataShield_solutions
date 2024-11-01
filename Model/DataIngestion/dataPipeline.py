import os
import asyncio
import json
import logging
from asyncpg import create_pool
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
from kafka.admin import KafkaAdminClient, NewTopic
from kafka.errors import KafkaError
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
DBUSER = os.getenv('DBUSER')
DBNAME = os.getenv('DBNAME')
DBPASSWORD = os.getenv('DBPASS')
DBHOST = os.getenv('DBHOST')
DBPORT = os.getenv('DBPORT')
KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS')

# Estimate the best number of partitions for the Kafka topic
def estimate_partitions(target_throughput, write_throughput, read_throughput):
    return max(target_throughput // write_throughput, target_throughput // read_throughput)

# Example usage
target = 10000  # messages per second
write = 100  # messages per second per partition
read = 150  # messages per second per partition
estimated_partitions = estimate_partitions(target, write, read)
logger.info(f"Estimated number of partitions: {estimated_partitions}")


# Kafka admin client to create a topic
try:
    admin_client = KafkaAdminClient(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        client_id='my-admin-client'
    )
    logger.info("Successfully connected to Kafka cluster")
except KafkaError as e:
    logger.error(f"Failed to connect to Kafka cluster: {e}")
    admin_client = None

if admin_client:
    topic = NewTopic(name='kenyaDataProtectionAct', num_partitions=estimated_partitions, replication_factor=1)
    try:
        admin_client.create_topics(new_topics=[topic])
        logger.info("Topic created successfully")
    except KafkaError as e:
        logger.error(f"Failed to create topic: {e}")
    finally:
        admin_client.close()

# Connect to PostgreSQL and fetch data
async def connect_to_postgres_and_fetch_data():
    pool = await create_pool(
        user=DBUSER,
        password=DBPASSWORD,
        database=DBNAME,
        host=DBHOST,
        port=DBPORT,
        ssl=False
    )
    async with pool.acquire() as conn:
        data = await conn.fetch("SELECT * FROM compliance_data")
    return data

# Produce data to Kafka
async def produce_to_kafka(data):
    producer = AIOKafkaProducer(
        bootstrap_servers=[KAFKA_BOOTSTRAP_SERVERS],
        value_serializer=lambda x: json.dumps(x).encode('utf-8')
    )
    await producer.start()
    try:
        for row in data:
            await producer.send('kenyaDataProtectionAct', value=dict(row))
        await producer.flush()
    except KafkaError as e:
        logger.error(f"Failed to send message to Kafka: {e}")
    finally:
        await producer.stop()

# Consume data from Kafka
async def consume_from_kafka():
    consumer = AIOKafkaConsumer(
        'kenyaDataProtectionAct',
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        auto_offset_reset='earliest',
        consumer_timeout_ms=1000,
        enable_auto_commit=False,
        group_id="compliance_group",
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    await consumer.start()
    try:
        logger.info("Starting to consume messages...")
        async for message in consumer:
            logger.info(f"Received message: {message.value}")
    except KafkaError as e:
        logger.error(f"Failed to consume message from Kafka: {e}")
    finally:
        await consumer.stop()

# Main function to run producer and consumer
async def main():
    try:
        data = await connect_to_postgres_and_fetch_data()
        await produce_to_kafka(data)
        await consume_from_kafka()
    except Exception as e:
        logger.error(f"An error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
