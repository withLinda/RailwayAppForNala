import pandas as pd
from dash import Dash, dash_table, dcc, html, Input, Output, State

df = pd.read_csv('profile_data1.csv')  # Read the csv file
app = Dash(__name__)
server = app.server

dtable = dash_table.DataTable(  # Create the table
    data=df.to_dict('records'),
    columns=[{'id': x, 'name': x, 'presentation': 'markdown'} if x == 'upworkUrl' else {'id': x, 'name': x} for x in
             df.columns],  # Set the columns
    # columns = [
    #     {'id' : 'No', 'name' : 'No'},
    #     {'id' : 'name', 'name' : 'Name'},
    #     {'id' : 'city', 'name' : 'City'},
    #     {'id' : 'title', 'name' : 'Title'},
    #     {'id' : 'description', 'name' : 'Description'},
    #     {'id' : 'totalEarnings', 'name' : 'Total Earnings', 'type' : 'numeric', 'format' : money},
    #     {'id' : 'totalHoursBilled', 'name' : 'Total Hours Billed'},
    #     {'id' : 'earningPerHour', 'name' : 'Earning Per Hour', 'type' : 'numeric', 'format' : money},
    #     {'id' : 'totalPortfolio', 'name' : 'Total Portfolio'},
    #     {'id' : 'upworkUrl', 'name' : 'Upwork Url', 'presentation' : 'markdown'}
    # ],
    style_cell={'textAlign': 'left',
                "backgroundColor": "#FDF5E6",
                "color": "#7FDBFF",
                "fontSize": 12,
                # "font-family": "helvetica",
                # "font-family": "sans-serif",
                "font-family": "Calibri",
                # 'fontFamily': 'Open Sans',
                "padding": "10px",
                "borderRadius": "10px",
                "border": "thin solid #FFFFFF"},  # Set the style of the cells
    style_header={'backgroundColor': '#FDF5E6', 'color': '#1A2E43', 'fontWeight': 'bold', 'textAlign': 'center',
                  'border': '1px solid black', "font-family": "Calibri" },  # Set the style of the header
    filter_action="native",  # Set the filter action
    # style_table={"overflowX": "auto"},      # Set the style of the table
    sort_action="native",  # Set the sort action
    sort_mode="multi",  # Set the sort mode
    row_deletable=True,
    style_data={  # Set the style of the data
        'whiteSpace': 'normal',
        'backgroundColor': '#1A2E43',
        'color': '#7FDBFF'
    },
    style_data_conditional=[  # Set the style of the data conditionally
        {
            'if': {'row_index': 'odd'},  # Set the style of the odd rows
            'backgroundColor': 'rgb(0, 51, 77)',
            'color': '#7FDBFF'
        },
        {
            "if": {"state": "selected"},  # Set the style of the selected rows
            'backgroundColor': '#FDF5E6',
            'color': '#333333'
            # "border": "inherit !important",
        }
    ],
    style_table={'borderRadius': '10px', 'overflowX': 'scroll', 'overflowY': 'auto'}

)
download_button = html.Button("Download Filtered CSV",
                              style={'font-size': '12px',
                                     'fontweight': 'bold',
                                     'color': '#7FDBFF',
                                     'width': '160px',
                                     'display': 'inline-block',
                                     'margin-bottom': '10px',#1A2E43
                                     "font-family": "Calibri",
                                     'margin-right': '5px',
                                     'height': '37px',
                                     'border': "thin solid #1A2E43",
                                     'borderRadius': '10px',
                                     'backgroundColor': 'rgb(0, 51, 77)',
                                     'verticalAlign': 'top'})
download_component = dcc.Download()

app.layout = html.Div(
    [
        download_component,
        download_button,
        dtable,
    ]
)


@app.callback(
    Output(download_component, "data"),
    Input(download_button, "n_clicks"),
    State(dtable, "derived_virtual_data"),
    prevent_initial_call=True,
)
def download_data(n_clicks, data):
    dff = pd.DataFrame(data)
    return dcc.send_data_frame(dff.to_csv, "filtered_csv.csv")


if __name__ == '__main__':
    app.run_server(debug=True)
