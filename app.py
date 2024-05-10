from flask import Flask, render_template
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

# 環境変数から設定を読み込む
app.config['MYSQL_HOST'] = os.getenv('DB_HOST', 'default_host')
app.config['MYSQL_USER'] = os.getenv('DB_USER', 'root')
app.config['MYSQL_PASSWORD'] = os.getenv('DB_PASS', 'default_password')
app.config['MYSQL_DB'] = os.getenv('DB_NAME', 'default_db')

mysql = MySQL(app)

@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT name FROM users")
    names = cursor.fetchall()
    cursor.close()
    return render_template('index.html', names=names)

if __name__ == '__main__':
    app.run(host='localhost',port=5000, debug=True)
