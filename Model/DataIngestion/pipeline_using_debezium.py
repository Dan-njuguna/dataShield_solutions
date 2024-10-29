import asyncpg
import asyncio
import psycopg2
import pyspark
import os
import ssl
import pandas as pd
from aiokafka import AIOKafkaConsumer, AIOKafkaProducer
from dotenv import load_dotenv
import json
from kafka import KafkaAdminClient
from kafka.admin import NewTopic
from kafka.errors import KafkaError
from datetime import datetime

# Estimating best number of partitions of the new topic
def estimate_partitions(target_throughput, write_throughput, read_throughput):
    return max(target_throughput // write_throughput, target_throughput // read_throughput)

# Example usage
target = 10000  # messages per second
write = 4000    # messages per second per partition
read = 5000     # messages per second per partition
estimated_partitions = estimate_partitions(target, write, read)
print(f"Estimated number of partitions: {estimated_partitions}")

topic = 'localhost.public.sample_data'

async def creation_using_debezium(topic):
    admin_client = KafkaAdminClient(bootstrap_servers="localhost:9092", client_id="myAdmin")
    all_topics = admin_client.list_topics()
    try:
        print("Successfully connected to cluster")   
        if topic not in all_topics:
            topic_obj = NewTopic(name=topic, num_partitions=estimated_partitions, replication_factor=3)
            admin_client.create_topics([topic_obj])
            print("Topic created successfully")
        else:
            print("Topic already exists")
    except KafkaError as e:
        print(f"Failed to connect to Kafka cluster: {e}")
    finally:
        admin_client.close()

async def consume_from_kafka(topic):
    """
    This function connects to a Kafka broker and consumes messages.
    """
    consumer = AIOKafkaConsumer(
        topic,
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    
    await consumer.start()
    messages = []
    try:
        print("Starting to consume messages...")
        async for message in consumer:
            # Parse ISO date strings back to date objects if needed
            parsed_message = {
                k: datetime.fromisoformat(v).date() if isinstance(v, str) and v.count('-') == 2 else v
                for k, v in message.value.items()
            }
            messages.append(parsed_message)
            print(f"Received message: {parsed_message}")
    except Exception as e:
        print(f"Error consuming messages: {e}")
    finally:
        await consumer.stop()
        return messages

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(creation_using_debezium(topic))
    messages = loop.run_until_complete(consume_from_kafka(topic))
    print(messages)
