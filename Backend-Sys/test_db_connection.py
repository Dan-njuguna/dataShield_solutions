import os
from dotenv import load_dotenv
from urllib.parse import urlparse
import pg8000

# Load environment variables from .env file
load_dotenv()

# Parse the DATABASE_URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable not set.")

# Parse the DATABASE_URL
tmpPostgres = urlparse(DATABASE_URL)

# Attempt to connect to the database
try:
    conn = pg8000.connect(
        user=tmpPostgres.username,
        password=tmpPostgres.password,
        host=tmpPostgres.hostname,
        port=tmpPostgres.port or 5432,
        database=tmpPostgres.path[1:]  # Remove leading slash
    )
    cursor = conn.cursor()
    cursor.execute("SELECT 1;")  # Simple query to test the connection
    result = cursor.fetchone()
    print("Connection successful! Result:", result)
except Exception as e:
    print("Error connecting to the database:", e)
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()