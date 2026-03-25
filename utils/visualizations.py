import plotly.express as px
import plotly.graph_objects as go


def plot_bar_chart(data, title, xlabel, ylabel):
    """
    Generates a bar chart from the given data.

    Parameters:
    data (dict): A dictionary where keys are categories and values are their respective values.
    title (str): The title of the chart.
    xlabel (str): The label for the x-axis.
    ylabel (str): The label for the y-axis.

    Returns:
    plotly.graph_objects.Figure
    """
    fig = px.bar(
        x=list(data.keys()),
        y=list(data.values()),
        title=title,
        labels={'x': xlabel, 'y': ylabel},
    )
    return fig


def plot_line_chart(data, title, xlabel, ylabel):
    """
    Generates a line chart from the given data.

    Parameters:
    data (dict): A dictionary where keys are data points and values are their respective values.
    title (str): The title of the chart.
    xlabel (str): The label for the x-axis.
    ylabel (str): The label for the y-axis.

    Returns:
    plotly.graph_objects.Figure
    """
    fig = px.line(
        x=list(data.keys()),
        y=list(data.values()),
        title=title,
        labels={'x': xlabel, 'y': ylabel},
    )
    return fig


def plot_pie_chart(data, title):
    """
    Generates a pie chart for the given data.

    Parameters:
    data (dict): A dictionary where keys are categories and values are their respective proportions.
    title (str): The title of the chart.

    Returns:
    plotly.graph_objects.Figure
    """
    fig = px.pie(
        names=list(data.keys()),
        values=list(data.values()),
        title=title,
    )
    return fig
