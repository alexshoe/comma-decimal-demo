from dash.dependencies import Input, Output, State
import dash_design_kit as ddk
import dash_core_components as dcc
import dash_html_components as html
import dash_table

from app import app
import pages
import utils

server = app.server


app.layout = ddk.App(
    [
        ddk.Header(
            [
                ddk.Title("Comma Decimal Demo"),
                ddk.Menu(
                    [
                        dcc.Link(href=app.get_relative_path("/"), children="Home"),
                    ],
                ),
            ]
        ),
        dcc.Location(id="url"),
        html.Div(id="content"),
    ],
)


@app.callback(
    Output("content", "children"),
    Input("url", "pathname"),
)
def display_content(pathname):
    page_name = app.strip_relative_path(pathname)

    if not page_name:  # None or ''
        return pages.home.layout()
    else:
        return "404"


if __name__ == "__main__":
    app.run_server(debug=True)
