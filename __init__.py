from flask import Flask, render_template, request, redirect, url_for, session
import os
from flaskr import db
import sqlite3
from flaskr.db import delete_user_by_email  # db.py の関数をインポート

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # セッションに必要

db.create_users_table()

@app.route('/')
def index():
    if 'user' in session:
        return render_template('index.html', email=session['user'])
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        db.add_user(email, password)
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = db.get_user(email, password)
        if user:
            session['user'] = email
            return redirect(url_for('index'))
        else:
            return 'ログイン失敗'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


@app.route('/delete_user', methods=['POST'])
def delete_user():
    email_to_delete = request.form['email']
    
    # db.py の関数を使って削除
    delete_user_by_email(email_to_delete)
    
    return redirect(url_for('index'))  # 削除後にindexページにリダイレクト