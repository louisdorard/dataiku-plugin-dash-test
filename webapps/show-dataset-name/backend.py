from dataiku.customwebapp import *

# Access the parameters that end-users filled in using webapp config
# For example, for a parameter called "input_dataset"
# input_dataset = get_webapp_config()["input_dataset"]

from dash import html
import dataiku

ds = dataiku.Dataset("iris")
df = ds.get_dataframe()

app.layout = html.Div([
    html.H4('Edit ' + ds.full_name)
])
