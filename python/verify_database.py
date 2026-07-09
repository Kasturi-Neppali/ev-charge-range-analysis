
import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("database/ev_database.db")

cursor = conn.cursor()

# Get all table names
cursor.execute("""
SELECT name
FROM sqlite_master
WHERE type='table';
""")

tables = cursor.fetchall()

print("\n========= DATABASE TABLES =========\n")

for table in tables:
    table_name = table[0]

    print(f"Table : {table_name}")

    query = f"SELECT COUNT(*) FROM {table_name}"

    count = pd.read_sql(query, conn)

    print(count)

    print("-" * 40)

conn.close()

print("\nDatabase Verification Completed Successfully!")
