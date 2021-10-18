import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output, State

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
)

app.title = "Comma Decimal Demo App"


def format_number(number, comma_or_point):
    readable_number = f"{float(number):,}"
    if comma_or_point == "comma":
        try:
            from string import maketrans  # Python 2
        except ImportError:
            maketrans = str.maketrans
        readable_number = readable_number.translate(maketrans(",.", ".,"))
        return readable_number
    else:
        return readable_number


app.layout = html.Div(
    [
        html.H1("Decimal Seperator Demo App"),
        dcc.Location(id="url", refresh=False),
        html.Div(
            children=[
                html.Div(
                    [
                        "This is a demo app to demonstrate how to implement commas as decimal seperators in a Dash app",
                        html.P(),
                        html.Div(
                            [
                                "Select your desired decimal format: ",
                                dcc.RadioItems(
                                    id="decimal-format",
                                    value="comma",
                                    options=[
                                        {"label": "Comma Decimal", "value": "comma"},
                                        {"label": "Point Decimal", "value": "point"},
                                    ],
                                ),
                            ]
                        ),
                    ],
                    style={
                        "width": "800px",
                        "border": "2px solid black",
                        "padding": "20px",
                        "margin": "20px",
                        "border-radius": "10px",
                    },
                ),
                html.Div(
                    children=[
                        html.Div(
                            "Change the value in the input box to see reformatting in action:",
                            style={"font-weight": "bold"},
                        ),
                        html.P(),
                        html.Div(
                            [
                                "Input: ",
                                dcc.Input(id="my-input", value="0", type="number"),
                            ]
                        ),
                        html.Br(),
                        html.Div(
                            id="my-output",
                        ),
                    ],
                    style={
                        "width": "800px",
                        "border": "2px solid black",
                        "padding": "20px",
                        "margin": "20px",
                        "border-radius": "10px",
                    },
                ),
            ]
        ),
    ]
)


@app.callback(
    Output("my-output", "children"),
    Input("my-input", "value"),
    Input("decimal-format", "value"),
)
def update_output_div(input_value, decimal_format):
    return f"Output: {format_number(input_value, decimal_format)}"


if __name__ == "__main__":
    app.run_server(debug=True)
