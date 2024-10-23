import unittest
import asyncio
from unittest.mock import patch
from dataPipeline import query_db, connect_db

class TestDataPipeline(unittest.TestCase):
    @patch('dataPipeline.connect_db')
    @patch('dataPipeline.asyncpg')
    async def test_query_db_concurrent(self, mock_asyncpg, mock_connect_db):
        mock_conn = mock_connect_db.return_value.__aenter__.return_value
        mock_cursor = mock_conn.cursor.return_value
        mock_cursor.__aenter__.return_value = mock_cursor
        mock_cursor.fetchall.side_effect = [[1, 2, 3], [4, 5, 6]]

        user_query = "SELECT * FROM users WHERE id IN %s"
        database_query = "SELECT id FROM users"

        result = await query_db(user_query, database_query)

        self.assertEqual(result, [(4, 5, 6)])
        mock_connect_db.assert_awaited_once()
        mock_conn.cursor.assert_awaited_once()
        mock_cursor.execute.assert_any_call(database_query)
        mock_cursor.fetchall.assert_any_call()
        mock_cursor.execute.assert_any_call(user_query, [(1, 2, 3)])
        mock_cursor.fetchall.assert_any_call()
        mock_conn.close.assert_called_once()

if __name__ == '__main__':
    asyncio.run(unittest.main())