import psycopg2
from config import load_config

def create_table():
    create_table_command = """
    CREATE TABLE phonebook (
        id SERIAL PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        phone VARCHAR(20) NOT NULL
    );
    """
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute(create_table_command)

if __name__ == '__main__':
    create_table()
