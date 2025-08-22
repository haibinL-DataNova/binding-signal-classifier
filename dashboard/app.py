import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

df = pd.read_csv('../data/sample_signals.csv')

fig = px.line(df, x='timestamp', y='signal_value', color='label')

app.layout = html.Div([
    html.H1("Biosensor Signal Viewer"),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
