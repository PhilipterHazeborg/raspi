from flask import Flask, send_file
import sqlite3
import charts

connection = sqlite3.connect("temperatur.db", check_same_thread=False)
cursor = connection.cursor()

app = Flask(__name__)


@app.route('/')
def hello_world():
    charts.charts()
    return send_file('static/chart.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000')
