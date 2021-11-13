import dash
from dash import html
from dash import dcc
from data_processing import serve_dataframe
from figure_factory import serve_figure
import datetime

app = dash.Dash(__name__, title='Global Climate Laws', 
                external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

server = app.server

def serve_layout(): # Called on page reload
    dataframe = serve_dataframe()  # Fetch data from Google Sheets
    fig = serve_figure(dataframe)  # Create a figure
    date = datetime.datetime.now().strftime("%d %B %Y, %H:%M")
    layout = html.Div([
            html.H1("Climate Laws Scrapers Tracking"),
            html.H2(f"Updated {date} (UTC+00:00)"),
            dcc.Graph(figure=fig, id='globe')
        ], id="main-container")
    return layout  # Return the layout

app.layout = serve_layout

if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_hot_reload=False)  # Remove debug for deployment!
