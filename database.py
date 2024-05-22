import sqlite3

def connect_to_db():
    conn = sqlite3.connect('db/coffee_shop.db')
    cursor = conn.cursor()
    return conn, cursor
