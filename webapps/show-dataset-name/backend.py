from dataiku.customwebapp import *


from dash import html
import dataiku

ds = get_webapp_config()["input_dataset"]

app.layout = html.Div([
    html.H4('Edit ' + ds.full_name)
])
