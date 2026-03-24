# dashboard/app.py
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# Load anomalies CSV from S3
df = pd.read_csv('https://your-s3-bucket/signal-anomalies/anomalies.csv')

app = Dash(__name__)

fig = px.scatter(df, x='timestamp', y='signal_value', color='anomaly',
                 title="Signal Values with Anomalies Highlighted")

app.layout = html.Div([
    html.H1("Signal Intelligence Dashboard"),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)