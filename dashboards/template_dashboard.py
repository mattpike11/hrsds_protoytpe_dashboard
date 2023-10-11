"""
A test bar chart dashboard
"""
from dash import Output, Input, html
import pandas as pd

from uk_gov_dash_components.Dropdown import Dropdown
from gov_uk_dashboards.components.plotly.filter_panel import filter_panel
from gov_uk_dashboards.components.plotly.main_content import main_content
from gov_uk_dashboards.components.plotly.row_component import row_component
from gov_uk_dashboards.components.plotly.visualisation_title import (
    format_visualisation_title,
)
from gov_uk_dashboards.components.plotly.visualisation_commentary import (
    format_visualisation_commentary,
)
from gov_uk_dashboards.components.plotly.card import card
from gov_uk_dashboards.components.plotly.graph import graph

from app import app

from figures.bar_chart import bar_chart


def template_dashboard(example_dropdown):
    """Create and return the dashboard layout for display in the application."""
    if example_dropdown is None:
        example_dropdown = "GENDER"

    # Read dummy data from local file into a data frame
    df = (
        pd.read_csv("data\example_data.csv")
        .groupby(example_dropdown)["PERSON_ID"]
        .count()
        .reset_index()
    )

    # Produce a bar chart from the data frame
    barchart = bar_chart(df, example_dropdown, "PERSON_ID", color=example_dropdown)
    barchart_dash = graph(
        element_id="example_bar_chart",
        figure=barchart,
    )
    dashboard_content = [card(barchart_dash)]

    return main_content(
        [
            filter_panel(
                [
                    Dropdown(
                        label="Example dropdown",
                        id="example_dropdown",
                        source=[
                            {"label": metric, "value": metric}
                            for metric in ["GENDER", "OUTCOME"]
                        ],
                        value=example_dropdown,
                    ),
                ],
            ),
            format_visualisation_title("My example graph"),
            html.Div(
                id="example_commentary",
            ),
            row_component(dashboard_content),
        ],
    )


# Write a callback function to update both the commentary and the bar chart
@app.callback(
    Output(component_id="example_commentary", component_property="children"),
    Output(component_id="example_bar_chart", component_property="figure"),
    Input(component_id="example_dropdown", component_property="value"),
)
def update_example_commentary_and_barchart(example_dropdown):
    """Example of how to update commentary with selected option."""
    # Create a new data frame with the updated dropdown selection
    updated_df = (
        pd.read_csv("data\example_data.csv")
        .groupby(example_dropdown)["PERSON_ID"]
        .count()
        .reset_index()
    )
    # Create a new bar chart with updated data frame
    updated_barchart = bar_chart(
        updated_df, example_dropdown, "PERSON_ID", color=example_dropdown
    )

    return (
        format_visualisation_commentary(f"{example_dropdown} selected."),
        updated_barchart,
    )
