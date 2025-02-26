import marimo

__generated_with = "0.11.7"
app = marimo.App(width="medium")


@app.cell
def _(df):
    countries_table = (
        df
        .groupby('CountryCode')
        .agg(
            impressions = ('Impressions', 'sum'),
            campaigns = ('ADID', 'count')
        )
        .sort_values('campaigns', ascending=False)
    )

    countries_table
    return (countries_table,)


@app.cell
def _(df):
    (
        df
        .assign(
            StartDate = lambda df: df.StartDate.dt.to_period('m')
        )
        .pivot_table(
            index = 'StartDate',
            columns = 'CountryCode',
            values = 'ADID',
            aggfunc = 'count' # lambda s: len(s.unique())
        )
        .plot
        .line(
            figsize=(15,10)
        )
    )
    return


@app.cell
def _(df):
    (
        df
        #.query('`Currency Code`=="EUR"')
        .assign(
            StartDate = lambda df: df.StartDate.dt.to_period('m')
        )
        .pivot_table(
            index = 'StartDate',
            columns = 'CountryCode',
            values = 'ADID',
            aggfunc = lambda s: len(s.unique())
        )
        .cumsum()
        .ffill()
        [[ "norway", "sweden", "france" ]]
        #[ countries_table.head(10).index.to_list() ]
        .plot
        .line(
            figsize=(15,10)
        )
    )
    return


@app.cell
def _(df):
    (
        df
        .query('`Currency Code`=="EUR"')
        .assign(
            StartDate = lambda df: df.StartDate.dt.to_period('m')
        )
        .pivot_table(
            index = 'StartDate',
            columns = 'CountryCode',
            values = 'ADID',
            aggfunc = lambda s: len(s.unique())
        )
        .cumsum()
        .ffill()
        [[ "france" ]]
        #[ countries_table.head(10).index.to_list() ]
        .plot
        .line(
            figsize=(15,10)
        )
    )
    return


@app.cell
def _(countries_table):
    (
        countries_table
        .plot
        .scatter(
            x = 'campaigns',
            y = 'impressions',
        )
    )
    return


@app.cell
def _(df):
    (
        df
        .query('`Currency Code` == "EUR"')
        .plot
        .scatter(
            x = 'Spend',
            y = 'Impressions',
            figsize=(15,10)
        )
    )
    return


@app.cell
def _(pd):
    df = (
        pd
        .read_csv('https://codeberg.org/dsa-datasprint-2025/notebooks/raw/branch/main/datasets/politicalads-2018-2025.csv')
        .assign(
            StartDate = lambda df: pd.to_datetime(df.StartDate),
            EndDate = lambda df: pd.to_datetime(df.EndDate)
        )
    )

    df
    return (df,)


@app.cell
def _():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    return np, pd, plt


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
