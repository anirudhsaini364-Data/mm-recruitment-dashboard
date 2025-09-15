import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Load your Excel data
df = pd.read_excel("recruitment_data.xlsx")

# Initialize Dash app
app = dash.Dash(__name__)

# KPI calculations
total_positions = df['Job Req ID'].nunique()
total_offers = df[df['Status'] == 'Offered'].shape[0]
joined = df[df['Status'] == 'Joined'].shape[0]
selection = df[df['Status'] == 'Selection'].shape[0]
in_process = df[df['Status'] == 'In Process'].shape[0]
reserve_ijp = df[df['Status'] == 'Reserve for IJP'].shape[0]
cancelled = df[df['Status'] == 'Cancelled'].shape[0]

# Charts
pie = px.pie(df, names='Department', values='Job Req ID', title='Hires by Department')
donut = px.pie(df, names='Source', values='Job Req ID', hole=0.5, title='Source Mix')

# Layout
app.layout = html.Div([
    html.H1("Mahindra & Mahindra Recruitment Dashboard", style={'color':'#E31C23'}),
    html.Div([
        html.Div([html.H4("Total Positions"), html.P(total_positions)], style={'padding':10, 'border':'1px solid black'}),
        html.Div([html.H4("Total Offers"), html.P(total_offers)], style={'padding':10, 'border':'1px solid black'}),
        html.Div([html.H4("Joined"), html.P(joined)], style={'padding':10, 'border':'1px solid black'}),
        html.Div([html.H4("Selection"), html.P(selection)], style={'padding':10, 'border':'1px solid black'}),
        html.Div([html.H4("In Process"), html.P(in_process)], style={'padding':10, 'border':'1px solid black'}),
        html.Div([html.H4("Reserve for IJP"), html.P(reserve_ijp)], style={'padding':10, 'border':'1px solid black'}),
        html.Div([html.H4("Cancelled"), html.P(cancelled)], style={'padding':10, 'border':'1px solid black'}),
    ], style={'display':'flex', 'justify-content':'space-between'}),
    html.Div([dcc.Graph(figure=pie), dcc.Graph(figure=donut)], style={'display':'flex'}),
])

if __name__ == '__main__':
    app.run_server(debug=True)
