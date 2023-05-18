from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)
data = pd.read_csv("data/Customer-Churn-Records.csv")

fig = px.scatter(data, x="Age of Customer", y="Duration of usage of credit card", color="Gender of Customer")



if __name__ == '__main__':
    app.run_server(debug=True)