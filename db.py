import sqlite3
import os

BASE_DIR = os.path.dirname(__file__)
DATABASE = os.path.join(BASE_DIR, 'users.db')

def create_users_table():
    con = sqlite3.connect(DATABASE)
    con.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    con.close()

def add_user(email, password):
    con = sqlite3.connect(DATABASE)
    con.execute('INSERT INTO users (email, password) VALUES (?, ?)', (email, password))
    con.commit()
    con.close()

def get_user(email, password):
    con = sqlite3.connect(DATABASE)
    user = con.execute('SELECT * FROM users WHERE email=? AND password=?', (email, password)).fetchone()
    con.close()
    return user

def delete_user_by_email(email):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # メールアドレスを指定して削除
    cursor.execute("DELETE FROM users WHERE email = ?", (email,))
    
    # 変更をコミットして接続を閉じる
    conn.commit()
    conn.close()