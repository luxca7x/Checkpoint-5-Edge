from dash import Dash, html, dcc, callback, Output, Input
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import requests

amount = 30
# Change IP To Current Host / Certifique-se de alterar o IP
URL = "http://4.228.227.153:8666/STH/v1/contextEntities/type/Lamp/id/urn:ngsi-ld:Lamp:006/attributes/"
PARAMS = {'lastN': amount}

# Headers as a dictionary
HEADERS = {
    'fiware-service': 'smart',
    'fiware-servicepath': '/'
}

app = Dash()

app.layout = html.Div(children=[
    html.H1(children='Checkpoint 5 Edge', style={'textAlign': 'center'}),
    dcc.Graph(id='graph-content'),
    dcc.Interval(id='interval-component', interval=1 * 1000, n_intervals=0)
])


@callback(
    Output('graph-content', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_graph_live(value):
    # Fetch data for luminosity
    r_luminosity = requests.get(url=URL + "luminosity", params=PARAMS, headers=HEADERS)
    data_luminosity = r_luminosity.json()
    data_luminosity = data_luminosity['contextResponses'][0]['contextElement']['attributes'][0]['values']

    # Fetch data for humidity
    r_humidity = requests.get(url=URL + "humidity", params=PARAMS, headers=HEADERS)
    data_humidity = r_humidity.json()
    data_humidity = data_humidity['contextResponses'][0]['contextElement']['attributes'][0]['values']

    # Fetch data for temperature
    r_temperature = requests.get(url=URL + "temperature", params=PARAMS, headers=HEADERS)
    data_temperature = r_temperature.json()
    data_temperature = data_temperature['contextResponses'][0]['contextElement']['attributes'][0]['values']

    # Create lists to store data
    luminosity_rows = []
    humidity_rows = []
    temperature_rows = []

    # Parse luminosity data
    for entry in data_luminosity:
        luminosity_rows.append([entry['recvTime'], float(entry['attrValue'])])

    # Parse humidity data
    for entry in data_humidity:
        humidity_rows.append([entry['recvTime'], float(entry['attrValue'])])

    # Parse temperature data
    for entry in data_temperature:
        temperature_rows.append([entry['recvTime'], float(entry['attrValue'])])

    # Create DataFrames for each attribute
    df_luminosity = pd.DataFrame(luminosity_rows, columns=['Time', 'Luminosity'])
    df_humidity = pd.DataFrame(humidity_rows, columns=['Time', 'Humidity'])
    df_temperature = pd.DataFrame(temperature_rows, columns=['Time', 'Temperature'])

    # Convert 'Time' to datetime and ensure all values are numeric
    df_luminosity['Time'] = pd.to_datetime(df_luminosity['Time'])
    df_luminosity['Luminosity'] = pd.to_numeric(df_luminosity['Luminosity'], errors='coerce')

    df_humidity['Time'] = pd.to_datetime(df_humidity['Time'])
    df_humidity['Humidity'] = pd.to_numeric(df_humidity['Humidity'], errors='coerce')

    df_temperature['Time'] = pd.to_datetime(df_temperature['Time'])
    df_temperature['Temperature'] = pd.to_numeric(df_temperature['Temperature'], errors='coerce')

    # Merge dataframes on Time and handle NaN values by interpolation
    df = pd.merge(df_luminosity, df_humidity, on='Time', how='outer')
    df = pd.merge(df, df_temperature, on='Time', how='outer')

    df = df.interpolate()  # Option to interpolate missing values
    df = df.fillna(0)  # Fill any remaining NaN values with 0

    # Create a figure with secondary y-axes
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add luminosity trace
    fig.add_trace(
        go.Scatter(x=df['Time'], y=df['Luminosity'], name="Luminosity", mode='lines'),
        secondary_y=False
    )

    # Add humidity trace
    fig.add_trace(
        go.Scatter(x=df['Time'], y=df['Humidity'], name="Humidity", mode='lines'),
        secondary_y=True
    )

    # Add temperature trace
    fig.add_trace(
        go.Scatter(x=df['Time'], y=df['Temperature'], name="Temperature", mode='lines'),
        secondary_y=True
    )

    # Set axis titles
    fig.update_xaxes(title_text="Time")
    fig.update_yaxes(title_text="Luminosity", secondary_y=False)
    fig.update_yaxes(title_text="Humidity / Temperature", secondary_y=True)

    # Update the layout
    fig.update_layout(title="Luminosity, Humidity, and Temperature Over Time")

    return fig


if __name__ == '__main__':
    app.run(debug=True)
