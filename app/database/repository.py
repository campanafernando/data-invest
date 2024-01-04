def insert_comment(conn, symbol, comment):
    sql = '''INSERT INTO comments(symbol, comment) VALUES(?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, (symbol, comment))
    conn.commit()

def get_comments(conn, symbol):
    cur = conn.cursor()
    cur.execute("SELECT * FROM comments WHERE symbol=?", (symbol,))
    rows = cur.fetchall()
    return rows