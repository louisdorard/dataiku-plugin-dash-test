from dataiku.customwebapp import *
from dash import html
from dataiku import Dataset

ds = Dataset(get_webapp_config()["input_dataset"])
app.layout = html.Div(ds.full_name)
