from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)
data = pd.read_csv("data/Customer-Churn-Records.csv")


if __name__ == '__main__':
    app.run_server(debug=True)