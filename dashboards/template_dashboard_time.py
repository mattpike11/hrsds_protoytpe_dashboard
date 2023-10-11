"""
A test time series dashboard
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

from figures.time_series import time_series


def template_dashboard_time(example_dropdown_time):
    """Create and return the dashboard layout for display in the application."""
    if example_dropdown_time is None:
        example_dropdown_time = "APPLICATION_DATE"

    # Read dummy data from local file into a data frame
    df = pd.read_csv("data\example_data.csv")
    # Extract months as last 7 characters in string
    df["month"] = df[example_dropdown_time].str[-7:]
    # aggregate
    df = df.groupby("month")["PERSON_ID"].count().reset_index()

    # Produce a time series from the data frame
    timeseries = time_series(df, "month", "PERSON_ID")
    timeseries_dash = graph(
        element_id="example_time_series",
        figure=timeseries,
    )
    dashboard_content = [card(timeseries_dash)]

    return main_content(
        [
            filter_panel(
                [
                    Dropdown(
                        label="Example dropdown",
                        id="example_dropdown_time",
                        source=[
                            {"label": metric, "value": metric}
                            for metric in ["APPLICATION_DATE","OUTCOME_DATE",]
                        ],
                        value=example_dropdown_time,
                    ),
                ],
            ),
            format_visualisation_title("My example graph"),
            html.Div(
                id="example_commentary_time",
            ),
            row_component(dashboard_content),
        ],
    )


# Write a callback function to update both the commentary and the time series
@app.callback(
    Output(component_id="example_commentary_time", component_property="children"),
    Output(component_id="example_time_series", component_property="figure"),
    Input(component_id="example_dropdown_time", component_property="value"),
)
def update_example_commentary_time_and_timeseries(example_dropdown_time):
    """Example of how to update commentary with selected option."""
    # Read dummy data from local file into a data frame
    df = pd.read_csv("data\example_data.csv")
    # Extract months as last 7 characters in string
    df["month"] = df[example_dropdown_time].str[-7:]
    # aggregate
    df = df.groupby("month")["PERSON_ID"].count().reset_index()
    
    # Create a new time series with updated data frame
    updated_timeseries = time_series(df, "month", "PERSON_ID")
    return (
        format_visualisation_commentary(f"{example_dropdown_time} selected."),
        updated_timeseries,
    )
