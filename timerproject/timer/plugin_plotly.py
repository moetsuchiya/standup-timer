#kakeibo/plugin_plotly.py
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
from datetime import timedelta


class GraphGenerator:
    """ビューから呼び出されて、グラフをhtmlにして返す"""

    def month_pie(self, labels, values):
        """月間のパイチャート"""
        hover_text = [f"{label}: {timedelta(seconds=value)}" for label, value in zip(labels, values)]

        fig = go.Figure(data=[go.Pie(
            labels=labels,
            values=values,
            hovertemplate="%{text}<br>%{percent}",
            text=hover_text
        )])

        fig.update_layout(
            title='カテゴリー別学習時間の割合',
            width=500,
            height=400,
            margin=dict(t=50, l=0, r=0, b=0)
        )

        return fig.to_html(full_html=False)

    def month_daily_bar(self, x_list, y_list):
        hover_text = [f"学習時間: {timedelta(seconds=y)}" for y in y_list]

        fig = go.Figure(data=[go.Bar(
            x=x_list,
            y=y_list,
            hovertemplate="日付: %{x}<br>%{text}",
            text=hover_text
        )])

        fig.update_layout(
            title='日別学習時間',
            xaxis_title='日付',
            yaxis_title='学習時間',
            width=1000,
            height=400,
            margin=dict(t=50, l=50, r=50, b=50)
        )

        return fig.to_html(full_html=False)