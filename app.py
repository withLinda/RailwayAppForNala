import dash_bootstrap_components as dbc
import pandas as pd
from dash import Dash, dash_table, dcc, html, Input, Output

# app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
df = pd.read_csv('profile_data2.csv')  # Read the csv file
jf = pd.read_csv('joblisting_data1.csv')  # Read the csv file

darkBlue_theme = {
    'background': '#14293a',
    'text': '#FFFFFF',
    'border': 'thin solid #14293a'
}

oddDarkBlue_theme = {
    'background': '#1D3B53',
    'text': '#FFFFFF',
    'border': 'thin solid #1D3B53'

}

creamBlack_theme = {
    'background': '#FDF5E6',
    'text': '#000000',
    'border': 'thin solid #FDF5E6'
}

font_theme = {
    "font-family": "Calibri"
}

dusk_theme = {
    'background': '#A74848',
    'text': '#FFFFFF',
    'border': 'thin solid #A74848'

}


class CustomDash(Dash):
    def interpolate_index(self, **kwargs):
        # Inspect the arguments by printing them
        print(kwargs)
        return '''
        <!DOCTYPE html>
        <html>
            <head>
                <script async src="https://analytics.umami.is/script.js" data-website-id="39feeba5-7f9e-474d-b1bd-9e6d088b0e31"></script>
                <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
                <meta charset="utf-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width,  initial-scale=1">
                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css">
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/js/bootstrap.min.js"></script>
                <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
                <title>For you..</title>
            </head>
            <body>

                <div id="custom-header"></div>
                {app_entry}
                {config}
                {scripts}
                {renderer}
                <div id="custom-footer"></div>
            </body>
        </html>
        '''.format(
            app_entry=kwargs['app_entry'],
            config=kwargs['config'],
            scripts=kwargs['scripts'],
            renderer=kwargs['renderer'])


app = CustomDash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {"position": "fixed", "top": 0, "left": 0, "bottom": 0, "width": "8rem", "padding": "2rem 1rem",
                 "background-color": creamBlack_theme['background'], "color": creamBlack_theme['text'],
                 "font-family": font_theme['font-family'], 'overflowY': 'auto', "fontSize": "1rem"}

SIDEBAR_TITLE_STYLE = {
    "font-size": "1.5rem",
    'fontWeight': 'bold',
    'textAlign': 'left',
}

SIDEBAR_TEXT_STYLE = {
    "font-size": "1rem",
    'textAlign': 'left',
}

SIDEBAR_NAVLINK_STYLE = {
    "background-color": dusk_theme['background'],
    "padding": "1rem 1rem",
    "margin-top": "1rem",
    "color": dusk_theme['text'],
    ":active": {"color": '#000000' },
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "9rem",
    "margin-right": "0rem",
    "padding": "0rem 0rem",
}

sidebar = html.Div(
    [
        html.H2("Hello there!", className="display-4", style=SIDEBAR_TITLE_STYLE),
        html.Hr(),
        html.P(
            "Pilih data yang ingin ditampilkan", className="lead", style=SIDEBAR_TEXT_STYLE
        ),
        dbc.Nav(
            [
                dbc.NavLink("Jobs List", href="/", active="exact", style=SIDEBAR_NAVLINK_STYLE),
                dbc.NavLink("Profiles", href="/profiles", active="exact", style=SIDEBAR_NAVLINK_STYLE),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

jtable = dash_table.DataTable(  # Create the table
    data=jf.to_dict('records'),
    columns=[{'id': x, 'name': x, 'presentation': 'markdown'} if x == 'job url' else {'id': x, 'name': x} for x in
             jf.columns],  # Set the columns
    style_cell={'textAlign': 'left',
                "backgroundColor": creamBlack_theme['background'],
                "color": creamBlack_theme['text'],
                "fontSize": 12,
                # "font-family": "helvetica",
                # "font-family": "sans-serif",
                "font-family": font_theme['font-family'],
                # 'fontFamily': 'Open Sans',
                "padding": "10px",
                "borderRadius": "10px",
                "border": creamBlack_theme['border']},  # Set the style of the cells
    style_header={'backgroundColor': dusk_theme['background'],
                  'color': dusk_theme['text'],
                  'fontWeight': 'bold',
                  'textAlign': 'center',
                  'border': dusk_theme['border'],
                  "font-family": font_theme['font-family']},  # Set the style of the header
    filter_action="native",  # Set the filter action
    # style_table={"overflowX": "auto"},      # Set the style of the table
    sort_action="native",  # Set the sort action
    sort_mode="multi",  # Set the sort mode
    row_deletable=True,
    cell_selectable=True,
    style_data={  # Set the style of the data
        'whiteSpace': 'normal',
        'backgroundColor': darkBlue_theme['background'],
        'color': darkBlue_theme['text'],
        'border': darkBlue_theme['border'],
    },
    style_data_conditional=[  # Set the style of the data conditionally
        {
            'if': {'row_index': 'odd'},  # Set the style of the odd rows
            'backgroundColor': oddDarkBlue_theme['background'],
            'color': oddDarkBlue_theme['text'],
            'border': oddDarkBlue_theme['border']
        },
        {
            "if": {"state": "selected"},  # Set the style of the selected rows
            'backgroundColor': dusk_theme['background'],
            'color': dusk_theme['text']
            # "border": "inherit !important",
        }
    ],
    style_table={'borderRadius': '10px', 'overflowX': 'scroll', 'overflowY': 'auto'}

)

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
                "backgroundColor": creamBlack_theme['background'],
                "color": creamBlack_theme['text'],
                "fontSize": 12,
                # "font-family": "helvetica",
                # "font-family": "sans-serif",
                "font-family": font_theme['font-family'],
                # 'fontFamily': 'Open Sans',
                "padding": "10px",
                "borderRadius": "10px",
                "border": creamBlack_theme['border']},  # Set the style of the cells
    style_header={'backgroundColor': dusk_theme['background'],
                  'color': dusk_theme['text'],
                  'fontWeight': 'bold',
                  'textAlign': 'center',
                  'border': dusk_theme['border'],
                  "font-family": font_theme['font-family']},  # Set the style of the header
    filter_action="native",  # Set the filter action
    # style_table={"overflowX": "auto"},      # Set the style of the table
    sort_action="native",  # Set the sort action
    sort_mode="multi",  # Set the sort mode
    row_deletable=True,
    cell_selectable=True,
    style_data={  # Set the style of the data
        'whiteSpace': 'normal',
        'backgroundColor': darkBlue_theme['background'],
        'color': darkBlue_theme['text'],
        'border': darkBlue_theme['border'],
    },
    style_data_conditional=[  # Set the style of the data conditionally
        {
            'if': {'row_index': 'odd'},  # Set the style of the odd rows
            'backgroundColor': oddDarkBlue_theme['background'],
            'color': oddDarkBlue_theme['text'],
            'border': oddDarkBlue_theme['border']
        },
        {
            "if": {"state": "selected"},  # Set the style of the selected rows
            'backgroundColor': dusk_theme['background'],
            'color': dusk_theme['text']
            # "border": "inherit !important",
        }
    ],
    style_table={'borderRadius': '10px', 'overflowX': 'scroll', 'overflowY': 'auto'}

)
download_button = html.Button("Download Filtered CSV",
                              style={'font-size': '12px',
                                     'fontweight': 'bold',
                                     'color': darkBlue_theme['text'],
                                     'width': '160px',
                                     'display': 'inline-block',
                                     'margin-bottom': '10px',  # 1A2E43
                                     "font-family": "Calibri",
                                     'margin-right': '5px',
                                     'height': '37px',
                                     'border': "thin solid #1A2E43",
                                     'borderRadius': '10px',
                                     'backgroundColor': darkBlue_theme['background'],
                                     'verticalAlign': 'top'})
download_component = dcc.Download()

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return jtable
    elif pathname == "/profiles":
        return dtable

    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )


if __name__ == "__main__":
    app.run_server(debug=True)
