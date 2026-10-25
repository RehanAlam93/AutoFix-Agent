"""
This module handles SQLite database connectivity and initialization
for storing code audit logs, input snippets, and refactored AI outputs.
"""

import os
import sqlite3

# Define the local SQLite database file path
DB_PATH = "autofix.db"


def get_db_connection() -> sqlite3.Connection | None:
  """Establish and return a connection to the SQLite database.

  Returns:
      sqlite3.Connection | None: A database connection object if successful,
      or None if connection fails.
  """
  try:
    # Connect to the local SQLite database file
    conn = sqlite3.connect(DB_PATH)
    # Configure row factory to access table columns by their string names
    conn.row_factory = sqlite3.Row
    return conn
  except Exception as e:
    print(f"Error connecting to SQLite: {e}")
    return None


def init_db() -> None:
  """Initialize the database schema and create the 'code_audits' table if it does not exist."""
  conn = get_db_connection()
  if conn is None:
    print("Failed to connect to SQLite database.")
    return

  cursor = conn.cursor()

  # SQL query to create the code audits table for storing session/audit history
  create_table_query = """
    CREATE TABLE IF NOT EXISTS code_audits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        input_code TEXT NOT NULL,
        detected_issues TEXT,
        refactored_code TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    """

  try:
    cursor.execute(create_table_query)
    conn.commit()
    print("SQLite Database table 'code_audits' created successfully!")
  except Exception as e:
    print(f"Error creating table: {e}")
  finally:
    # Ensure database cursor and connection are closed securely
    cursor.close()
    conn.close()


if __name__ == "__main__":
  init_db()