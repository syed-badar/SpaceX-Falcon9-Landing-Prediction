import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

spacex_df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_geo.csv")
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("SpaceX Launch Records Dashboard"),
    dcc.Dropdown(id='site-dropdown', 
                 options=[{'label': 'All Sites', 'value': 'ALL'}] + 
                         [{'label': i, 'value': i} for i in spacex_df['Launch Site'].unique()],
                 value='ALL'),
    dcc.Graph(id='success-pie-chart')
])

@app.callback(Output('success-pie-chart', 'figure'), Input('site-dropdown', 'value'))
def update_graph(site):
    if site == 'ALL':
        fig = px.pie(spacex_df, values='class', names='Launch Site', title='Total Success By Site')
    else:
        df = spacex_df[spacex_df['Launch Site'] == site]
        fig = px.pie(df, names='class', title=f'Success Rate for {site}')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)