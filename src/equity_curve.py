def build_equity_curve(df, initial_capital=100_000):
    equity = initial_capital + df["profit"].cumsum()
    peak = equity.cummax()

    return {
        "equity": equity,
        "drawdown": equity - peak,
        "drawdown_pct": (equity - peak) / peak
    }
