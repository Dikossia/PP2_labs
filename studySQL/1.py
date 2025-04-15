import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(
    dbname="for_study",  
    user="postgres",   
    password="dikossia06",  
    host="localhost",          
)

cursor = conn.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    user_name VARCHAR(100) NOT NULL,
    score INT DEFAULT 0
);
"""
cursor.execute(create_table_query)

conn.commit()

cursor.close()
conn.close()

print("Таблица 'users' успешно создана!")
