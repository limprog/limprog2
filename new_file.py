from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)
data = pd.read_csv("data/Customer-Churn-Records.csv")

fig = px.scatter(data, x="Age", y="Tenure", color="Gender")

app.layout = html.Div(children=[
    html.H1(children='ВОзраст и время'),
    dcc.Graph(figure={}, id="figure_1"),
    'X',
    dcc.Dropdown(
        ["Age", "Tenure", "Balance", "EstimatedSalary"],
        'Age', id='X'
    ),
    'Y',
    dcc.Dropdown(
        ["Age", "Tenure", "Balance", "EstimatedSalary"],
        'Balance', id="Y"
    ),
])

@app.callback(
    Output('figure_1', component_property='figure'),
    Input('X', 'value'),
    Input('Y', 'value')
)
def update_store_data(X, Y):
    fig = px.scatter(data, x=X, y=Y, color="Gender")
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)