import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    try:
        sql = '''CREATE TABLE IF NOT EXISTS comments (
                    id INTEGER PRIMARY KEY,
                    symbol TEXT NOT NULL,
                    comment TEXT NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                );'''
        conn.execute(sql)
    except sqlite3.Error as e:
        print(e)
