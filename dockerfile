FROM python:3.9

WORKDIR /app

# パッケージ
RUN pip install pymysql cryptography Flask Flask-MySQLdb

COPY . /app
