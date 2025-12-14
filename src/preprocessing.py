import pandas as pd


def build_trades(df: pd.DataFrame) -> pd.DataFrame:
    """
    Rebuild completed trades from MT5 IN/OUT rows.
    """

    trades = []

    open_trade = None

    for _, row in df.iterrows():

        if row["entry_type"] == "in":
            open_trade = row

        elif row["entry_type"] == "out" and open_trade is not None:

            trade = {
                "open_time": open_trade["time"],
                "close_time": row["time"],
                "symbol": row["symbol"],
                "side": open_trade["side"],
                "volume": open_trade["volume"],
                "open_price": open_trade["price"],
                "close_price": row["price"],
                "profit": row["profit"],
            }

            trades.append(trade)
            open_trade = None

    df_trades = pd.DataFrame(trades)

    # Holding time
    df_trades["holding_minutes"] = (
        df_trades["close_time"] - df_trades["open_time"]
    ).dt.total_seconds() / 60

    return df_trades
