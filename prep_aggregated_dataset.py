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
def _(mo):
    mo.md(r"""## harmonise les montants payés en euros""")
    return


@app.cell
def _():
    import currency_converter
    return (currency_converter,)


@app.cell
def _(currency_converter):
    c = currency_converter.CurrencyConverter(fallback_on_missing_rate=True)
    return (c,)


@app.cell
def _(c, df, pd):
    Spend_Euros = (
        df
        .assign(
            StartDate = lambda df: pd.to_datetime(df.StartDate)
        )
        .pipe(lambda df_: df_[df_.StartDate <= "2025-02-12"])
        .assign(
            StartDate = lambda df: df.StartDate.dt.date
        )
        .apply(
            lambda r: (
                c.convert(
                    amount=r["Spend"],
                    currency=r["Currency Code"],
                    date=r["StartDate"]
                )
            ), axis=1
        )
        .astype('int')
    )
    return (Spend_Euros,)


@app.cell
def _(Spend_Euros, df, pd):
    df_final = (
        df
        .assign(
            StartDate = lambda df: pd.to_datetime(df.StartDate)
        )
        .pipe(lambda df_: df_[df_.StartDate <= "2025-02-12"])
        .assign(
            Spend_Euros = Spend_Euros
        )
    )

    df_final
    return (df_final,)


@app.cell
def _(df_final):
    df_final.to_csv('datasets/politicalads-2018-20250212-alleuros.csv')
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
