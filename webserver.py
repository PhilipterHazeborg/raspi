from flask import Flask, send_file
import charts
import os

DIR = "static/"
app = Flask(__name__)
IP, PORT = '0.0.0.0', 8000


@app.route('/')
def main():
    charts.charts()
    return send_file('static/chart.html')


if __name__ == '__main__':
    os.makedirs(os.path.dirname(DIR), exist_ok=True)
    charts.init()
    app.run(host=IP, port=PORT)
