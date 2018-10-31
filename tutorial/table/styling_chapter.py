from collections import OrderedDict
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from textwrap import dedent

import dash_table
from .utils import html_table, section_title


data = OrderedDict(
    [
        ("Date", ["2015-01-01", "2015-10-24", "2016-05-10"] * 2),
        ("Region", ["Montreal", "Vermont", "New York City"] * 2),
        ("Temperature", [1, -20, 3.512] * 2),
        ("Humidity", [10, 20, 30] * 2),
        ("Pressure", [2, 10924, 3912] * 2),
    ]
)

df = pd.DataFrame(data)

data = OrderedDict(
    [
        (
            "Date",
            [
                "July 12th, 2013 - July 25th, 2013",
                "July 12th, 2013 - August 25th, 2013",
                "July 12th, 2014 - August 25th, 2014",
            ],
        ),
        (
            "Election Polling Organization",
            ["The New York Times", "Pew Research", "The Washington Post"],
        ),
        ("Rep", [1, -20, 3.512]),
        ("Dem", [10, 20, 30]),
        ("Ind", [2, 10924, 3912]),
        (
            "Region",
            [
                "Northern New York State to the Southern Appalachian Mountains",
                "Canada",
                "Southern Vermont",
            ],
        ),
    ]
)

df_election = pd.DataFrame(data)
df_long = pd.DataFrame(
    OrderedDict([(name, col_data * 10) for (name, col_data) in data.items()])
)


layout = html.Div(
    style={"marginLeft": "auto", "marginRight": "auto", "width": "80%"},
    children=[

        html.H1('Sizing Guide'),

        html.H1("Background - HTML Tables"),
        section_title("HTML Table - Default Styles"),
        html.Div("By default, HTML tables expand to their contents"),
        html_table(df_election, table_style={}, base_column_style={}),
        section_title("HTML Table - Padding"),

        html.Div(
        """
        Since the table content is packed so tightly,
        it's usually a good idea to place some left
        on the columns.
        """
        ),
        html_table(df_election, table_style={}, cell_style={"paddingLeft": 10}),

        section_title("HTML Table - Responsive Table"),
        html.Div(
        """
        With 100% width, the tables will expand to their
        container. When the table gets small, the text will break into
        multiple lines.
        """
        ),
        html_table(df_election, table_style={"width": "100%"}, base_column_style={}),

        section_title("HTML Table - All Column Widths defined by Percent"),
        html.Div(
        """
        The column widths can be definied by percents rather than pixels.
        """
        ),
        html_table(
            df_election,
            table_style={"width": "100%"},
            column_style={
                "Date": {"width": "30%"},
                "Election Polling Organization": {"width": "25%"},
                "Dem": {"width": "5%"},
                "Rep": {"width": "5%"},
                "Ind": {"width": "5%"},
                "Region": {"width": "30%"},
            },
        ),

        section_title("HTML Table - Single Column Width Defined by Percent"),
        html.Div(
        """
        The width of one column (Region=50%) can be definied by percent.
        """
        ),
        html_table(
            df_election,
            table_style={"width": "100%"},
            column_style={"Region": {"width": "50%"}},
        ),

        section_title("HTML Table - Columns with min-width"),
        html.Div(
        "Here, the min-width for the first column is 130px, or about the width of this line: "
        ),
        html.Div(
            style={"width": 130, "height": 10, "backgroundColor": "hotpink"}
        ),
        html_table(
            df_election,
            table_style={"width": "100%"},
            column_style={"Date": {"minWidth": "130"}},
        ),

        section_title("HTML Table - Underspecified Widths"),
        html.Div(
        """
        The widths can be under-specified. Here, we're only setting the width for the three
        columns in the middle, the rest of the columns are automatically sized to fit the rest of the container.
        The columns have a width of 50px, or the width of this line:
        """
        ),
        html.Div(
            style={"width": 50, "height": 10, "backgroundColor": "hotpink"}
        ),
        html_table(
            df_election,
            table_style={"width": "100%"},
            column_style={
                "Dem": {"width": 50},
                "Rep": {"width": 50},
                "Ind": {"width": 50},
            },
        ),

        section_title("HTML Table - Widths that are smaller than the content"),
        html.Div(
        """
        In this case, we're setting the width to 20px, which is smaller
        than the "10924" number in the "Ind" column.
        The table does not allow it.
        """
        ),
        html.Div(
            style={"width": 20, "height": 10, "backgroundColor": "hotpink"}
        ),
        html_table(
            df_election,
            table_style={"width": "100%"},
            column_style={
                "Dem": {"width": 20},
                "Rep": {"width": 20},
                "Ind": {"width": 20},
            },
        ),

        section_title("HTML Table - Content with Ellipses"),
        html.Div(
        """
        With `max-width`, the content can collapse into
        ellipses once the content doesn't fit.

        Here, `max-width` is set to 0. It could be any number, the only
        important thing is that it is supplied. The behaviour will be
            the same whether it is 0 or 50.
        """
        ),
        html_table(
            df_election,
            table_style={"width": "100%"},
            cell_style={
                "whiteSpace": "nowrap",
                "overflow": "hidden",
                "textOverflow": "ellipsis",
                "maxWidth": 0,
            },
        ),

        section_title("HTML Table - Vertical Scrolling"),
        html.Div(
        """
        By supplying a max-height of the Table container and supplying
        `overflow-y: scroll`, the table will become scrollable if the
        table's contents are larger than the container.
        """
        ),
        html.Div(
            style={"maxHeight": 300, "overflowY": "scroll"},
            children=html_table(df_long, table_style={"width": "100%"}),
        ),

        section_title("HTML Table - Vertical Scrolling with Max Height"),
        html.Div(
        """
        With `max-height`, if the table's contents are shorter than the
        `max-height`, then the container will be shorter.
        If you want a container with a constant height no matter the
        contents, then use `height`.

        Here, we're setting max-height to 300, or the height of this line:
        """
        ),
        html.Div(
            style={"width": 5, "height": 300, "backgroundColor": "hotpink"}
        ),
        html.Div(
            style={"maxHeight": 300, "overflowY": "scroll"},
            children=html_table(df_election, table_style={"width": "100%"}),
        ),

        section_title("HTML Table - Vertical Scrolling with Height"),
        html.Div("and here is `height` with the same content"),
        html.Div(
            style={"height": 300, "overflowY": "scroll"},
            children=html_table(df_election, table_style={"width": "100%"}),
        ),

        section_title("HTML Table - Horizontal Scrolling"),
        dcc.Markdown(dedent(
        """
        With HTML tables, we can set `min-width` to be 100%.
        If the content is small, then the columns will have some extra
        space.
        But if the content of any of the cells is really large, then the
        cells will expand beyond the container and a scrollbar will appear.

        In this way, `min-width` and `overflow-x: scroll` is an alternative
        to `text-overflow: ellipses`. With scroll, the content that can't
        fit in the container will get pushed out into a scrollable zone.
        With text-overflow: ellipses, the content will get truncated by
        ellipses. Both strategies work with or without line breaks on the
        white spaces (`white-space: normal` or `white-space: nowrap`).

        These next two examples have the same styles applied:
        - `min-width: 100%`
        - `white-space: nowrap` (to keep the content on a single line)
        - A parent with `overflow-x: scroll`

        """
        )),

        section_title("HTML Table - Two Columns, 100% Min-Width"),
        html.Div(
            html_table(
                pd.DataFrame({"Column 1": [1, 2], "Column 2": [3, 3]}),
                table_style={"minWidth": "100%"},
                cell_style={"whiteSpace": "nowrap"},
            ),
            style={"overflowX": "scroll"},
        ),

        section_title("HTML Table - Long Columns, 100% Min-Width"),
        html.Div(
        """
            Here is a table with several columns with long titles,
            100% min-width, and `'white-space': 'nowrap'`
            (to keep the text on a single line)
        """
        ),
        html.Div(
            html_table(
                pd.DataFrame(
                    {
                        "This is Column {} Data".format(i): [1, 2]
                        for i in range(10)
                    }
                ),
                table_style={"minWidth": "100%", "overflowX": "scroll"},
                cell_style={"whiteSpace": "nowrap"},
            ),
            style={"overflowX": "scroll"},
        ),
        html.Hr(),
        html.H3("Dash Interactive Table"),
        html.Div("These same styles can be applied to the dash table"),

        section_title("Dash Table - Default Styles"),
        dash_table.DataTable(
            id="sizing-1",
            data=df_election.to_dict("rows"),
            columns=[{"name": i, "id": i} for i in df_election.columns],
        ),

        section_title("Dash Table - Padding"),
        # ...

        section_title("Dash Table - All Column Widths by Percent"),
        html.Div(
        """
        Here is a table with all columns having width equal to 16.67%,
        the Region column additionally wraps text. The table will try and respect
        the width of each column while allowing for the content to be displayed.

        Changing the browser's viewport width will help understand how the table
        allocates space.
        """
        ),
        dash_table.DataTable(
            id="sizing-2",
            data=df_election.to_dict("rows"),
            content_style="grow",
            columns=[
                {"name": i, "id": i, "width": "16.67%"} for i in df_election.columns
            ],
            style_table=[
                {"selector": ".dash-spreadsheet", "rule": "width: 100%"},
                {
                    "selector": ".dash-cell[data-dash-column=Region]",
                    "rule": "white-space: normal",
                },
            ],
        ),

        section_title("Dash Table - Single Column Width by Percent"),
        html.Div(
        """
        Here is a table with all columns having default (auto) width excepts for the
        the Region column that has 50% width and wraps text. The table will try and respect
        the width of each column while allowing for the content to be displayed.

        Changing the browser's viewport width will help understand how the table
        allocates space.
        """
        ),
        dash_table.DataTable(
            id="sizing-3",
            data=df_election.to_dict("rows"),
            content_style="grow",
            columns=[
                {"name": i, "id": i, "width": "50%" if i == "Region" else None}
                for i in df_election.columns
            ],
            style_table=[
                {"selector": ".dash-spreadsheet", "rule": "width: 100%"},
                {
                    "selector": ".dash-cell[data-dash-column=Region]",
                    "rule": "white-space: normal",
                },
            ],
        ),

        section_title("Dash Table - Underspecified Widths"),
        html.Div(
        """
        The widths can be under-specified. Here, we're only setting the width for the three
        columns in the middle, the rest of the columns are automatically sized to fit the rest of the container.
        The columns have a width/minWidth/maxWidth of 100px.
        """
        ),
        dash_table.DataTable(
            id="sizing-4",
            data=df_election.to_dict("rows"),
            columns=[
                {
                    "name": i,
                    "id": i,
                    "width": "100px"
                    if i == "Dem" or i == "Rep" or i == "Ind"
                    else None,
                    "minWidth": "100px"
                    if i == "Dem" or i == "Rep" or i == "Ind"
                    else None,
                    "maxWidth": "100px"
                    if i == "Dem" or i == "Rep" or i == "Ind"
                    else None,
                }
                for i in df_election.columns
            ],
        ),

        section_title("Dash Table - Widths that are smaller than the content"),
        html.Div(
        """
        Width for all columns is set to 100px. Columns whose content is smaller than the defined size will respect it.
        Columns whose content is bigger than defined will grow to accomodate content. Region column wraps to show behavior
        in that case
        """
        ),
        dash_table.DataTable(
            id="sizing-5",
            data=df_election.to_dict("rows"),
            columns=[
                {"name": i, "id": i, "width": "100px"} for i in df_election.columns
            ],
            style_table=[
                {
                    "selector": ".dash-cell[data-dash-column=Region]",
                    "rule": "white-space: normal",
                }
            ],
        ),

        section_title(
            "Dash Table - Widths that are smaller than the content (forced)"
        ),
        html.Div(
        """
        Width/minWidth/maxWidth for all columns is set to 100px. Columns whose content is smaller than the defined size will respect it.
        Columns whose content is bigger than defined will respect it too. Region column wraps to show behavior
        in that case
        """
        ),
        dash_table.DataTable(
            id="sizing-6",
            data=df_election.to_dict("rows"),
            columns=[
                {
                    "name": i,
                    "id": i,
                    "width": "100px",
                    "minWidth": "100px",
                    "maxWidth": "100px",
                }
                for i in df_election.columns
            ],
            style_table=[
                {
                    "selector": ".dash-cell[data-dash-column=Region]",
                    "rule": "white-space: normal",
                }
            ],
        ),

        html.Hr(),

        html.H1("Styling the Dash Table"),

        section_title("HTML Table - Gridded"),

        html.Div(
        """
        By default, the Dash table has grey headers and borders
        around each cell. It resembles a spreadsheet with clearly defined
        headers
        """
        ),

        html_table(
            df,
            cell_style={'border': 'thin lightgrey solid'},
            table_style={'width': '100%'},
            column_style={'width': '20%', 'paddingLeft': 20},
            header_style={'backgroundColor': 'rgb(235, 235, 235)'}
        ),

        html.Hr(),

        section_title("HTML Table - Column Alignment and Column Fonts"),
        dcc.Markdown(dedent(
        """
        When displaying numerical data, it's a good practice to use
        monospaced fonts, to right-align the data, and to provide the same
        number of decimals throughout the column.

        Note that it's not possible to modify the number of decimal places
        in css. `dash-table` will provide formatting options in the future,
        until then you'll have to modify your data before displaying it.

        For textual data, left-aligning the data is usually easier to read.

        In both cases, the column headers should have the same alignment
        as the cell content.
        """
        )),
        html_table(
            df,
            table_style={'width': '100%'},
            column_style={'width': '20%', 'paddingLeft': 20},
            cell_style={"paddingLeft": 5, "paddingRight": 5, 'border': 'thin lightgrey solid'},
            header_style_by_column={
                "Temperature": {"textAlign": "right", "fontFamily": "monospaced"},
                "Humidity": {"textAlign": "right", "fontFamily": "monospaced"},
                "Pressure": {"textAlign": "right", "fontFamily": "monospaced"},
            },
            cell_style_by_column={
                "Temperature": {"textAlign": "right", "fontFamily": "monospaced"},
                "Humidity": {"textAlign": "right", "fontFamily": "monospaced"},
                "Pressure": {"textAlign": "right", "fontFamily": "monospaced"},
            },
            header_style={'backgroundColor': 'rgb(235, 235, 235)'}
        ),

        html.Hr(),

        section_title('HTML Table - Styling the Table as a List'),

        dcc.Markdown(dedent('''
        The gridded view is a good default view for an editable table, like a spreadsheet.
        If your table isn't editable, then in many cases it can look cleaner without the
        horizontal or vertical grid lines.
        ''')),

        html_table(
            df,
            table_style={'width': '100%'},
            column_style={'width': '20%', 'paddingLeft': 20},
            cell_style={"paddingLeft": 5, "paddingRight": 5},
            header_style={'backgroundColor': 'rgb(235, 235, 235)', 'borderTop': 'thin lightgrey solid', 'borderBottom': 'thin lightgrey solid'},
            header_style_by_column={
                "Temperature": {"textAlign": "right", "fontFamily": "monospaced"},
                "Humidity": {"textAlign": "right", "fontFamily": "monospaced"},
                "Pressure": {"textAlign": "right", "fontFamily": "monospaced"},
            },
            cell_style_by_column={
                "Temperature": {"textAlign": "right", "fontFamily": "monospaced"},
                "Humidity": {"textAlign": "right", "fontFamily": "monospaced"},
                "Pressure": {"textAlign": "right", "fontFamily": "monospaced"},
            },
        ),

        html.Hr(),

        section_title('HTML Table - Row Padding'),

        dcc.Markdown(dedent('''
        By default, the gridded view is pretty tight. You can add some top and bottom row padding to
        the rows to give your data a little bit more room to breathe.
        ''')),

        html_table(
            df,
            table_style={'width': '100%'},
            column_style={'width': '20%', 'paddingLeft': 20},
            cell_style={"paddingLeft": 5, "paddingRight": 5},
            header_style={'backgroundColor': 'rgb(235, 235, 235)', 'borderTop': 'thin lightgrey solid', 'borderBottom': 'thin lightgrey solid'},
            header_style_by_column={
                "Temperature": {"textAlign": "right", "fontFamily": "monospaced"},
                "Humidity": {"textAlign": "right", "fontFamily": "monospaced"},
                "Pressure": {"textAlign": "right", "fontFamily": "monospaced"},
            },
            cell_style_by_column={
                "Temperature": {"textAlign": "right", "fontFamily": "monospaced"},
                "Humidity": {"textAlign": "right", "fontFamily": "monospaced"},
                "Pressure": {"textAlign": "right", "fontFamily": "monospaced"},
            },
            row_style={'paddingTop': 10, 'paddingBottom': 10}
        ),

        html.Hr(),

        section_title('HTML Table - List Style with Minimal Headers'),

        dcc.Markdown(dedent('''
        In some contexts, the grey background can look a little heavy.
        You can lighten this up by giving it a white background and
        a thicker bottom border.
        ''')),

        html_table(
            df,
            table_style={'width': '100%'},
            column_style={'width': '20%', 'paddingLeft': 20},
            cell_style={"paddingLeft": 5, "paddingRight": 5},
            header_style={'borderBottom': '2px lightgrey solid'},
            header_style_by_column={
                "Temperature": {"textAlign": "right", "fontFamily": "monospaced"},
                "Humidity": {"textAlign": "right", "fontFamily": "monospaced"},
                "Pressure": {"textAlign": "right", "fontFamily": "monospaced"},
            },
            cell_style_by_column={
                "Temperature": {"textAlign": "right", "fontFamily": "monospaced"},
                "Humidity": {"textAlign": "right", "fontFamily": "monospaced"},
                "Pressure": {"textAlign": "right", "fontFamily": "monospaced"},
            },
            row_style={'paddingTop': 10, 'paddingBottom': 10}
        ),

        html.Hr(),

        section_title('HTML Table - List Style with Understated Headers'),

        dcc.Markdown(dedent('''
        When the data is obvious, sometimes you can de-emphasize the headers
        as well, by giving them a lighter color than the cell text.
        ''')),

        html_table(
            df,
            table_style={'width': '100%'},
            column_style={'width': '20%', 'paddingLeft': 20},
            cell_style={"paddingLeft": 5, "paddingRight": 5},
            header_style={'color': 'rgb(100, 100, 100)'},
            header_style_by_column={
                "Temperature": {"textAlign": "right", "fontFamily": "monospaced"},
                "Humidity": {"textAlign": "right", "fontFamily": "monospaced"},
                "Pressure": {"textAlign": "right", "fontFamily": "monospaced"},
            },
            cell_style_by_column={
                "Temperature": {"textAlign": "right", "fontFamily": "monospaced"},
                "Humidity": {"textAlign": "right", "fontFamily": "monospaced"},
                "Pressure": {"textAlign": "right", "fontFamily": "monospaced"},
            },
            row_style={'paddingTop': 10, 'paddingBottom': 10}
        ),

        html.Hr(),

        section_title('HTML Table - Striped Rows'),

        dcc.Markdown(dedent('''
        When you're viewing datasets where you need to compare values within individual rows, it
        can sometimes be helpful to give the rows alternating background colors.
        We recommend using colors that are faded so as to not attract too much attention to the stripes.
        ''')),

        html_table(
            df,
            table_style={'width': '100%'},
            column_style={'width': '20%', 'paddingLeft': 20},
            cell_style={"paddingLeft": 5, "paddingRight": 5},
            header_style={'backgroundColor': 'rgb(235, 235, 235)', 'borderTop': 'thin lightgrey solid', 'borderBottom': 'thin lightgrey solid'},
            header_style_by_column={
                "Temperature": {"textAlign": "right", "fontFamily": "monospaced"},
                "Humidity": {"textAlign": "right", "fontFamily": "monospaced"},
                "Pressure": {"textAlign": "right", "fontFamily": "monospaced"},
            },
            cell_style_by_column={
                "Temperature": {"textAlign": "right", "fontFamily": "monospaced"},
                "Humidity": {"textAlign": "right", "fontFamily": "monospaced"},
                "Pressure": {"textAlign": "right", "fontFamily": "monospaced"},
            },
            row_style={'paddingTop': 10, 'paddingBottom': 10},
            odd_row_style={'backgroundColor': 'rgb(248, 248, 248)'}
        ),

        section_title('HTML Table - Dark Theme with Cells'),

        dcc.Markdown(dedent(
        """
        You have full control over all of the elements in the table.
        If you are viewing your table in an app with a dark background,
        you can provide inverted background and font colors.
        """
        )),

        html_table(
            df,
            table_style={
                'backgroundColor': 'rgb(50, 50, 50)',
                'color': 'white',
                'width': '100%'
            },
            cell_style={'border': 'thin white solid'},
            header_style={'backgroundColor': 'rgb(30, 30, 30)'},
            row_style={'padding': 10},
            header_style_by_column={
                "Temperature": {"textAlign": "right", "fontFamily": "monospaced"},
                "Humidity": {"textAlign": "right", "fontFamily": "monospaced"},
                "Pressure": {"textAlign": "right", "fontFamily": "monospaced"},
            },
            cell_style_by_column={
                "Temperature": {"textAlign": "right", "fontFamily": "monospaced"},
                "Humidity": {"textAlign": "right", "fontFamily": "monospaced"},
                "Pressure": {"textAlign": "right", "fontFamily": "monospaced"},
            },
        ),

        section_title('HTML Table - Dark Theme with Rows'),

        html_table(
            df,
            table_style={
                'backgroundColor': 'rgb(50, 50, 50)',
                'color': 'white',
                'width': '100%'
            },
            row_style={
                'borderTop': 'thin white solid',
                'borderBottom': 'thin white solid',
                'padding': 10
            },
            header_style={'backgroundColor': 'rgb(30, 30, 30)'},
            header_style_by_column={
                "Temperature": {"textAlign": "right", "fontFamily": "monospaced"},
                "Humidity": {"textAlign": "right", "fontFamily": "monospaced"},
                "Pressure": {"textAlign": "right", "fontFamily": "monospaced"},
            },
            cell_style_by_column={
                "Temperature": {"textAlign": "right", "fontFamily": "monospaced"},
                "Humidity": {"textAlign": "right", "fontFamily": "monospaced"},
                "Pressure": {"textAlign": "right", "fontFamily": "monospaced"},
            },
        ),

        section_title('HTML Table - Highlighting Certain Rows'),

        dcc.Markdown(dedent('''
        You can draw attention to certain rows by providing a unique
        background color, bold text, or colored text.
        ''')),

        html_table(
            df,
            cell_style={'border': 'thin lightgrey solid', 'color': 'rgb(60, 60, 60)'},
            table_style={'width': '100%'},
            column_style={'width': '20%', 'paddingLeft': 20},
            header_style={'backgroundColor': 'rgb(235, 235, 235)'},
            row_style_by_index={
                4: {
                    'backgroundColor': 'yellow',
                }
            }
        ),

        section_title('HTML Table - Highlighting Certain Columns'),

        dcc.Markdown(dedent('''
        Similarly, certain columns can be highlighted.
        ''')),

        html_table(
            df,
            cell_style={'border': 'thin lightgrey solid', 'color': 'rgb(60, 60, 60)'},
            table_style={'width': '100%'},
            column_style={'width': '20%', 'paddingLeft': 20},
            header_style={'backgroundColor': 'rgb(235, 235, 235)'},
            cell_style_by_column={
                "Temperature": {
                    "backgroundColor": "yellow"
                },
            }
        ),

        section_title('HTML Table - Highlighting Certain Cells'),

        dcc.Markdown(dedent('''
        You can also highlight certain cells. For example, you may want to
        highlight certain cells that exceed a threshold or that match
        a filter elsewhere in the app.
        ''')),

        html_table(
            df,
            cell_style={'border': 'thin lightgrey solid', 'color': 'rgb(60, 60, 60)'},
            table_style={'width': '100%'},
            column_style={'width': '20%', 'paddingLeft': 20},
            header_style={'backgroundColor': 'rgb(235, 235, 235)'},
            conditional_cell_style=lambda cell, column: (
                {'backgroundColor': 'yellow'}
                if (
                    (column == 'Region' and cell == 'Montreal')
                    or
                    (cell == 20)
                ) else {}
            )
        ),

        section_title('Multi-Headers'),

        dash_table.DataTable(
            id='multi-headers',
            columns=[
                {"name": ["Year", ""], "id": "year"},
                {"name": ["City", "Montreal"], "id": "montreal"},
                {"name": ["City", "Toronto"], "id": "toronto"},
                {"name": ["City", "Ottawa"], "id": "ottawa", "hidden": True},
                {"name": ["City", "Vancouver"], "id": "vancouver"},
                {"name": ["Climate", "Temperature"], "id": "temp"},
                {"name": ["Climate", "Humidity"], "id": "humidity"},
            ],
            data=[
                {
                    "year": i,
                    "montreal": i * 10,
                    "toronto": i * 100,
                    "ottawa": i * -1,
                    "vancouver": i * -10,
                    "temp": i * -100,
                    "humidity": i * 0.1,
                }
                for i in range(100)
            ],
            merge_duplicate_headers=True,
        )

    ]
)
