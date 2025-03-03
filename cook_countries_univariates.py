import marimo

__generated_with = "0.11.7"
app = marimo.App(width="full")


@app.cell(hide_code=True)
def _(mo):
    mo.md("""# metrics by country""")
    return


@app.cell(hide_code=True)
def _(df, metrics_radio, mo, plot_static, show_outliers, table_ui):
    mo.hstack([
        metrics_radio,
        mo.vstack([
            table_ui,
            plot_static(df.query('CountryCode.isin(@table_ui.value.index.to_list())')),
            show_outliers
            #plot(df.query('CountryCode.isin(@table_ui.value.index.to_list())'))
        ])
    ])
    return


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
        .read_csv('https://raw.githubusercontent.com/taniki/dsa-datasprint-group7-notebooks/refs/heads/main/datasets/politicalads-2018-20250212-alleuros.csv')
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
    mo.md("""## graphics""")
    return


@app.cell
def _():
    from pyobsplot import Plot
    return (Plot,)


@app.cell
def _(metrics_radio, plt, show_outliers):
    def plot_static(df):
        fig, ax = plt.subplots(figsize=(15,3))

        if (len(df) > 0):
            (
                df
                .plot
                .box(
                    column=metrics_radio.value,
                    by="CountryCode",
                    showfliers=show_outliers.value,
                    ax=ax
                )
            )
        #plt.show()

        return fig
    return (plot_static,)


@app.cell
def _(df, plot_static):
    plot_static(df.query('CountryCode.isin(@table_ui.value.index.to_list())'))
    return


@app.cell
def _():
    import matplotlib.pyplot as plt
    return (plt,)


@app.cell
def _(Plot, metrics_radio):
    def plot(data):    
        return Plot.plot({
            "marginLeft": 100,
            "y": {"grid": True},
            "x": {
                "label": None,
            },
            # color: {legend: true},
            "marks": [
                Plot.dot(data, Plot.dodgeX("middle", {"fx": "CountryCode", "y": metrics_radio.value}))
            ]
        })

    #plot(df.query('CountryCode.isin(@table_ui.value.index.to_list())'))
    return (plot,)


@app.cell
def _(table_ui):
    table_ui.value.index.to_list()
    return


@app.cell
def _(df):
    df.query('CountryCode.isin(@table_ui.value.index.to_list())')
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
def _(df, metrics_radio, mo):
    table = (
        df
        .groupby('CountryCode')
        [ metrics_radio.value ]
        .agg(['count', 'sum', 'mean', 'std', 'median'])
        .sort_values('mean', ascending=False)
    )

    def format_float(x):
        return '{:.2f}'.format(x) if metrics_radio.value != 'cost_per_impression' else '{:.4f}'.format(x)

    table_ui = mo.ui.table(
        table,
        #selection=None,
        format_mapping={
            'mean': format_float,
            'std': format_float,
            'median': format_float,
        }
    )

    return format_float, table, table_ui


@app.cell
def _(mo):
    show_outliers = mo.ui.checkbox(label="display outliers")
    return (show_outliers,)


@app.cell
def _(show_outliers):
    (show_outliers, show_outliers.value)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
