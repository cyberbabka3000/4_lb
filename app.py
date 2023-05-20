import requests
from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    database = 'service_db',
    user = 'postgres',
    password = 'Dan12345',
    host = 'localhost',
    port = '5432'
)

cursor = conn.cursor()


@app.route('/login/', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if not username or not password:
        return render_template('login.html', error="Чо, самый умный?")

    cursor.execute("SELECT * FROM users WHERE login=%s AND password=%s", (str(username), str(password)))
    record = list(cursor.fetchall())

    if record:
        return render_template('account.html', full_name=record[0][1], login=record[0][2], password=record[0][3])
    else:
        return render_template('login.html',error="Пользователя не существует, либо пароль неверный")

@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')
