import psycopg2

# Connect to the PostgreSQL database
def connect_to_db():
    conn = psycopg2.connect(
        host="localhost",
        database="telecom",
        user="user",
        password="123456"
    )
    return conn

# Query the database
def query_db(query):
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows