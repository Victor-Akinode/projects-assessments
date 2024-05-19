import psycopg2
from psycopg2 import sql

# Database connection parameters
DB_NAME = "victor_akinode_db"
DB_USER = "victor_akinode_user"
DB_PASSWORD = "VictorDBPassword"
DB_HOST = "localhost"
DB_PORT = "5434"

def count_records():
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        
        # Create a new database session and return a new instance of the connection class
        cur = conn.cursor()
        
        # Define the query to count the number of records
        query = sql.SQL("SELECT COUNT(*) FROM {}.{}").format(
            sql.Identifier('ASSIGNMENT'),
            sql.Identifier('AUTOS')
        )
        
        # Execute the query
        cur.execute(query)
        
        # Fetch the result
        count = cur.fetchone()[0]
        
        print(f"Number of records in the AUTOS table: {count}")
        
        # Close the cursor and connection
        cur.close()
        conn.close()
        
    except Exception as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    count_records()
