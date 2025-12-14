import numpy as np
import pandas as pd


def monte_carlo_trades(
    df,
    initial_capital=100_000,
    simulations=10_000
):
    pnl = df["profit"].values
    results = []

    for _ in range(simulations):
        shuffled = np.random.permutation(pnl)
        equity = initial_capital + np.cumsum(shuffled)

        results.append({
            "final_equity": equity[-1],
            "max_drawdown": (equity - equity.cummax()).min()
        })

    return pd.DataFrame(results)
