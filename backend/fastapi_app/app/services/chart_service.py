import pandas as pd
import plotly.express as px


def select_chart(result):

    if not result:
        return "table"

    df = pd.DataFrame(result)

    if len(df.columns) == 2:

        second_column = df.columns[1]

        if pd.api.types.is_numeric_dtype(df[second_column]):
            return "bar"

    return "table"


def create_chart(result, chart_type):

    if not result or chart_type == "table":
        return None

    df = pd.DataFrame(result)

    if chart_type == "bar":

        x_column = df.columns[0]
        y_column = df.columns[1]

        fig = px.bar(
            df,
            x=x_column,
            y=y_column,
            title=f"{y_column} by {x_column}"
        )

        return fig