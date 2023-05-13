import plotly.graph_objects as go
import numpy as np

from .kuramoto import Kuramoto


def plot_activity(activity):
    """
    Plot sin(angle) vs time for each oscillator time series.

    activity: 2D-np.ndarray
        Activity time series, node vs. time; ie output of Kuramoto.run()
    return:
        Plotly figure object for further customization
    """
    fig = go.Figure()
    time = np.arange(activity.shape[1])
    for i in range(activity.shape[0]):
        fig.add_trace(go.Scatter(x=time, y=np.sin(activity[i]), mode='lines', name=f"Node {i+1}"))
    fig.update_layout(
        xaxis_title='Time',
        yaxis_title=r'$\sin(\theta)$',
        height=400,
        width=1000,
        font=dict(size=20),
        showlegend=True,
    )
    return fig


def plot_phase_coherence(activity):
    """
    Plot order parameter phase_coherence vs time.

    activity: 2D-np.ndarray
        Activity time series, node vs. time; ie output of Kuramoto.run()
    return:
        Plotly figure object for further customization
    """
    order_params = [Kuramoto.phase_coherence(vec) for vec in activity.T]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=np.arange(len(order_params)), y=order_params, mode='lines', name='Order parameter'))
    fig.update_layout(
        xaxis_title='Time',
        yaxis_title='Order parameter',
        height=300,
        width=800,
        font=dict(size=18),
        showlegend=False,
        yaxis_range=[-0.01, 1]
    )
    return fig
