import marimo

__generated_with = "0.11.7"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md("""# metrics by country""")
    return


@app.cell
def _(df, metrics_radio, mo):

    table = (
        df
        .groupby('CountryCode')
        [ metrics_radio.value ]
        .describe()
        .sort_values('count', ascending=False)
    )

    mo.hstack([
        metrics_radio,
        table
    ])
    return (table,)


@app.cell
def _(mo):
    mo.md("""## libraries""")
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import pandas as pd
    return (pd,)


@app.cell
def _(mo):
    mo.md("""## data""")
    return


@app.cell
def _(pd):
    df = (
        pd
        .read_csv('https://codeberg.org/dsa-datasprint-2025/notebooks/raw/branch/main/datasets/politicalads-2018-20250212-alleuros.csv')
        .assign(
            StartDate = lambda df: pd.to_datetime(df.StartDate),
            EndDate = lambda df: pd.to_datetime(df.EndDate)
        )
        .assign(
            cost_per_impression = lambda df: df.Spend_Euros / df.Impressions
        )
    )

    df
    return (df,)


@app.cell
def _(df):
    df.columns
    return


@app.cell
def _(mo):
    mo.md("""## UI helpers""")
    return


@app.cell
def _():
    metrics = [
        'Spend_Euros',
        'Impressions',
        'cost_per_impression',
    ]
    return (metrics,)


@app.cell
def _(metrics, mo):
    metrics_radio = mo.ui.radio(metrics, value="Spend_Euros")
    return (metrics_radio,)


@app.cell
def _(metrics_radio):
    metrics_radio
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
