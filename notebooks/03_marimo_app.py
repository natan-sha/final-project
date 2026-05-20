import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium", app_title="Final project")


@app.cell
def _():
    # Cell 1 — imports
    import marimo as mo
    import pandas as pd
    import plotly.express as px

    return mo, pd, px


@app.cell
def _(pd):
    panel = pd.read_csv(
        "/Users/nataliam/Documents/Claude/Projects/German hospitals/data/processed/panel.csv"
    )
    panel.head()
    return (panel,)


@app.cell
def _(panel, px):
    fig = px.scatter(
        panel[panel["year"] == 2023],
        x="share_65_plus",
        y="hospitals_per_100k",
        hover_name="kreis_name",
        title="Hospital access in 2023",
    )
    fig
    return


@app.cell
def _(mo):
    year_picker = mo.ui.dropdown(
        options=[2011, 2015, 2019, 2023],
        value=2023,
        label="Pick a year:",
    )
    year_picker
    return (year_picker,)


@app.cell
def _(year_picker):
    year = year_picker.value

    return


@app.cell
def _(mo):
    mo.md("""
    ## How has hospital access changed across aging cohorts?

    The trajectory below splits Kreise into four groups by their 2011 aging level
    and shows how each group's median hospital count evolved through 2023.
    """)
    return


@app.cell
def _(panel, pd, px):
    baseline = (
        panel[panel["year"] == 2011]
        [["kreis_code", "share_65_plus"]]
        .rename(columns={"share_65_plus": "aging_2011"})
    )
    baseline["aging_quartile"] = pd.qcut(
        baseline["aging_2011"],
        q=4,
        labels=["Q1 (youngest 25%)", "Q2", "Q3", "Q4 (oldest 25%)"],
    )

    # 2. Tag each panel row with its Kreis's 2011 quartile
    panel_q = panel.merge(baseline[["kreis_code", "aging_quartile"]], on="kreis_code")

    # 3. Compute absolute hospital count per-capita access per (quartile, year)
    trajectory_abs = (
        panel_q
        .groupby(["aging_quartile", "year"])["n_hospitals"]
        .median()
        .reset_index()
    )
    # 4. Plot the trajectories
    fig2 = px.line(
        trajectory_abs,
        x="year",
        y="n_hospitals",
        color="aging_quartile",
        markers=True,                            # show each year's point
        title="Absolute hospital access by 2011 aging quartile, 2011 → 2023",
        labels={
            "year": "Year",
            "n_hospitals": "Median number of hospitals per Kreis",
            "aging_quartile": "Aging cohort (2011)",
        },
        color_discrete_sequence=["#3B82F6", "#60A5FA", "#F87171", "#C8385C"],
        # blue → cherry: visually conveys "younger → older"
    )
    # Removing the default title
    fig2.update_layout(title=None, margin=dict(t=40, b=100, l=60, r=200))

    # New title — inside the plot
    fig2.add_annotation(
        text="<b>An apparent sharp change in access to hospitals in 2019, for all but the youngest regions </b>",
        xref="paper", yref="paper",
        x=0.49, y=1.07,
        xanchor="center", yanchor="top",
        showarrow=False,
        font=dict(size=15, color="#191240"),
    )

    fig2.add_annotation(
        text=("The popular narrative that aging German regions have disproportionately been losing <br>hospital access is not supported by the data</i>"),
        xref="paper", yref="paper",
        x=0.4, y=0.78,
        xanchor="center", yanchor="top",
        showarrow=False,
        font=dict(size=11, color="#555"),
        bgcolor="rgba(255,255,255,0.85)",
        bordercolor="lightgray",
        borderwidth=1,
        borderpad=8,
    )

    # Source — small gray text under the chart
    fig2.add_annotation(
        text=("Source: Destatis Krankenhausverzeichnis· "
              "Regionalstatistik table 12411-03-03-4."
        ),
        xref="paper", yref="paper",
        x=0.6, y=-0.25,
        xanchor="left",
        showarrow=False,
        font=dict(size=10, color="gray"),
    )

    fig2.add_vrect(
        x0=2019, x1=2023,
        fillcolor="gray", opacity=0.09,
        line_width=0,
        annotation_text="Growth of 28% within 4 years <br>Suspected change in reporting",
        annotation_position="top left",
        annotation=dict(font=dict(size=11, color="dark gray")),
    )

    fig2.show()
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A similar tendency with a sudden growth of hospital access after 2019 can be observed if counted per-capita
    """)
    return


@app.cell
def _(panel, pd):
    import plotly.express as px3

    # 1. Get each Kreis's baseline aging in 2011, assign it to a quartile
    baseline3 = (
        panel[panel["year"] == 2011]
        [["kreis_code", "share_65_plus"]]
        .rename(columns={"share_65_plus": "aging_2011"})
    )
    baseline3["aging_quartile"] = pd.qcut(
        baseline3["aging_2011"],
        q=4,
        labels=["Q1 (youngest 25%)", "Q2", "Q3", "Q4 (oldest 25%)"],
    )

    # 2. Tag each panel row with its Kreis's 2011 quartile
    panel_q3 = panel.merge(baseline3[["kreis_code", "aging_quartile"]], on="kreis_code")

    # 3. Compute median per-capita access per (quartile, year)
    trajectory = (
        panel_q3
        .groupby(["aging_quartile", "year"])["hospitals_per_100k"]
        .median()
        .reset_index()
    )

    # 4. Plot the trajectories
    fig3 = px3.line(
        trajectory,
        x="year",
        y="hospitals_per_100k",
        color="aging_quartile",
        markers=True,                            # show each year's point
        title="Median hospital access by 2011 aging quartile, 2011 → 2023",
        labels={
            "year": "Year",
            "hospitals_per_100k": "Median hospitals per 100,000 residents",
            "aging_quartile": "Aging cohort (2011)",
        },
        color_discrete_sequence=["#3B82F6", "#60A5FA", "#F87171", "#C8385C"],
        # blue → cherry: visually conveys "younger → older"
    )
    # Removing the default title
    fig3.update_layout(title=None, margin=dict(t=40, b=100, l=60, r=200))

    # New title — inside the plot
    fig3.add_annotation(
        text="<b>Apparent post-2019 rise in older Kreise's per-capita hospital access</b>",
        xref="paper", yref="paper",
        x=0.45, y=1.07,#0.937,
        xanchor="center", yanchor="top",
        showarrow=False,
        font=dict(size=15, color="#191240"),
    )

    fig3.add_annotation(
        text=("Question stays. Is the pattern real or<br> is it inflated by a change in Destatis' facility-level reporting in 2023?</i>"),
        xref="paper", yref="paper",
        x=0.4, y=0.84,
        xanchor="center", yanchor="top",
        showarrow=False,
        font=dict(size=11, color="#555"),
        bgcolor="rgba(255,255,255,0.85)",
        bordercolor="lightgray",
        borderwidth=1,
        borderpad=8,
    )

    # Source — small gray text under the chart
    fig3.add_annotation(
        text=("Source: Destatis Krankenhausverzeichnis· "
              "Regionalstatistik table 12411-03-03-4."
        ),
        xref="paper", yref="paper",
        x=0.6, y=-0.25,
        xanchor="left",
        showarrow=False,
        font=dict(size=10, color="gray"),
    )
    fig3.show()
    return


if __name__ == "__main__":
    app.run()


