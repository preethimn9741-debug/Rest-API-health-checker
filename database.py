import sqlite3

DB = "data.db"

def get_connection():
    return sqlite3.connect(DB)

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def get_all_items():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM items")
    rows = cur.fetchall()
    conn.close()
    return [{"id": r[0], "name": r[1]} for r in rows]

def add_item(name):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO items (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

def delete_item(item_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM items WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()

init_db()
