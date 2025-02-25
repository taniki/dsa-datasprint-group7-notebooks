import marimo

__generated_with = "0.11.7"
app = marimo.App(width="medium")


@app.cell
def _():
    source = '../snapchat-politicalads'
    return (source,)


@app.cell
def _(dd, source):
    df = (
        dd
        .read_csv(f'{source}/*.csv', dtype='object')
        .compute()
    )

    df
    return (df,)


@app.cell
def _(df):
    df.to_csv('datasets/politicalads-2018-2025.csv')
    return


@app.cell
def _():
    import dask.dataframe as dd
    import pandas as pd
    return dd, pd


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
