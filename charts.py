import plotly.graph_objects as go
from plotly.subplots import make_subplots
import sqlite3
import pandas as pd


def init():
    connection = sqlite3.connect("temperatur.db")
    cursor = connection.cursor()
    print(cursor.execute("CREATE TABLE IF NOT EXISTS daten(date TEXT, temp REAL, hum REAL)").fetchall())
    connection.commit()


def charts():
    connection = sqlite3.connect("temperatur.db")
    cursor = connection.cursor()
    df = pd.DataFrame(cursor.execute("SELECT date, temp, hum FROM daten").fetchall(),
                      columns=['Datum', 'Temperatur', 'Feuchtigkeit'])
    df['Datum'] = pd.to_datetime(df['Datum'])

    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add traces
    fig.add_trace(
        go.Scatter(x=df['Datum'], y=df['Temperatur'], name="Temperatur"), secondary_y=False,)

    fig.add_trace(
        go.Scatter(x=df['Datum'], y=df['Feuchtigkeit'], name="Feuchtigkeit"), secondary_y=True,)

    # Add figure title
    fig.update_layout(
        title_text="Feuchtigkeit und Temperatur")

    # Set x-axis title
    fig.update_xaxes(title_text="Datum")

    # Set y-axes titles
    fig.update_yaxes(title_text="Temperatur", secondary_y=False)
    fig.update_yaxes(title_text="Feuchtigkeit", secondary_y=True)

    # Add range slider
    fig.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=10,
                         label="10 Min",
                         step="minute",
                         stepmode="backward"),
                    dict(step="all")
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
            type="date"
        )
    )

    fig.write_html('static/chart.html', auto_open=False)
