import plotly.express as px
import sqlite3
import pandas as pd


def charts():
    connection = sqlite3.connect("temperatur.db", check_same_thread=False)
    cursor = connection.cursor()
    df = pd.DataFrame(cursor.execute("SELECT date, temp, hum FROM daten").fetchall(), columns=['Datum', 'Temperatur', 'Hum'])
   
    fig = px.line(df, y='Temperatur', x='Datum', title='Temperatur und Feuchtigkeit', hover_name='Temperatur')
    fig.add_scatter(y=df['Hum'], x=df['Datum'])
    fig.write_html('static/chart.html', auto_open=False)
