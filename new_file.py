from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)
data = pd.read_csv("data/Customer-Churn-Records.csv")

fig = px.scatter(data, x="Age", y="Tenure", color="Gender")

app.layout = html.Div(children=[
    html.H1(children='ВОзраст и время'),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)