```python
import psycopg2
from psycopg2 import sql

# Database connection parameters
DB_NAME = "congressconnect_db"
DB_USER = "admin"
DB_PASS = "securepassword"
DB_HOST = "localhost"
DB_PORT = "5432"

# Connect to the database
conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)

# Create a cursor object
cur = conn.cursor()

# Create tables
tables = ['UserSchema', 'LegislationSchema', 'ConstituentSchema', 'CampaignSchema', 'EventSchema']

for table in tables:
    create_table_query = sql.SQL("CREATE TABLE IF NOT EXISTS {} (id SERIAL PRIMARY KEY, data JSONB NOT NULL)").format(sql.Identifier(table))
    cur.execute(create_table_query)

# Commit changes and close connection
conn.commit()
conn.close()
```