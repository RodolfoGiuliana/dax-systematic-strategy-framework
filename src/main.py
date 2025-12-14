from data_loader import load_mt5_xlsx
from preprocessing import build_trades
from equity_curve import build_equity_curve
from montecarlo import monte_carlo_trades


def run():
    raw = load_mt5_xlsx("data/raw/DAX_DAtiXLSX.xlsx")
    trades = build_trades(raw)

    equity = build_equity_curve(trades)
    mc = monte_carlo_trades(trades)

    print("Trades:", len(trades))
    print("Final Equity:", equity["equity"].iloc[-1])

    print("\nMonte Carlo percentiles:")
    print(mc.quantile([0.01, 0.05, 0.5]))


if __name__ == "__main__":
    run()
