import plotly.graph_objects as go
from datetime import date

devices = [
    {"name": "TCL RayNeo X2",  "date": date(2024, 5, 1),  "score": 0.16},
    {"name": "INMO Air3",      "date": date(2025, 11, 1), "score": 0.19},
    {"name": "RayNeo X3 Pro",  "date": date(2025, 12, 1), "score": 0.19},
]

dates  = [d["date"]  for d in devices]
scores = [d["score"] for d in devices]
names  = [d["name"]  for d in devices]

fig = go.Figure()

BG    = "#0f0f0f"
LINE  = "#e0e0e0"
GRID  = "#2a2a2a"
MUTED = "#888"
RED   = "#ff5c5c"

COLORS = ["#7eb8f7", "#f7a96e", "#6ee8a2"]
text_positions = ["top center", "bottom center", "top center"]

fig.add_trace(go.Scatter(
    x=dates,
    y=scores,
    mode="lines",
    line=dict(color=LINE, width=1.5),
    hoverinfo="skip",
))

for i, device in enumerate(devices):
    fig.add_trace(go.Scatter(
        x=[device["date"]],
        y=[device["score"]],
        mode="markers+text",
        text=[device["name"]],
        textposition=text_positions[i],
        textfont=dict(family="Inter, sans-serif", size=12, color=COLORS[i]),
        marker=dict(color=COLORS[i], size=9),
        hovertemplate=f"<b>{device['name']}</b><br>Score: {device['score']:.2f}<extra></extra>",
        cliponaxis=False,
        showlegend=False,
    ))

fig.add_hline(
    y=1.0,
    line=dict(color=RED, width=1.2, dash="dash"),
    annotation_text="good enough",
    annotation_position="top right",
    annotation_font=dict(color=RED, size=11),
)

fig.update_layout(
    plot_bgcolor=BG,
    paper_bgcolor=BG,
    font=dict(family="Inter, sans-serif", color=LINE),
    title=None,
    xaxis=dict(
        title="",
        showgrid=False,
        showline=True,
        linecolor=GRID,
        tickfont=dict(size=11, color=MUTED),
        tickformat="%b %Y",
    ),
    yaxis=dict(
        title="Score",
        range=[0, 1.3],
        showgrid=True,
        gridcolor=GRID,
        showline=False,
        tickfont=dict(size=11, color=MUTED),
        zeroline=False,
    ),
    margin=dict(l=50, r=40, t=20, b=50),
    width=800,
    height=420,
    showlegend=False,
)

fig.write_image("chart/chart.png", scale=2)
print("chart.png written")
