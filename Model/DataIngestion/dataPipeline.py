import kafka
import pyspark
import psycopg2
import asyncpg
from dotenv import load_dotenv
import os

load_dotenv()

# Database configuration information
DBUSER = os.getenv("DBUSER")
DBNAME = os.getenv("DBNAME")
DBPASS = os.getenv("DBPASS")
DBHOST = os.getenv("DBHOST")
DBPORT = os.getenv("DBPORT")

async def connect_db():
    '''Connects to the PostgreSQL Database.
    Returns connection
    '''
    return await psycopg2.create_pool(
        user=DBUSER,
        database=DBNAME,
        password=DBPASS,
        host=DBHOST,
        port=DBPORT,
    )

async def query_db(user_query, database_query):
    '''Executes a database query.
    Returns result
    '''
    conn = await connect_db()
    async with conn.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute(database_query)
            rows = await cur.fetchall()
            await cur.execute(user_query, rows)
            result = await cur.fetchall()
    conn.close()
    return result