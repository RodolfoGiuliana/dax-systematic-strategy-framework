import pandas as pd


def load_mt5_xlsx(path: str) -> pd.DataFrame:
    """
    Load Strategy Tester XLSX and extract raw trade rows.
    """

    df = pd.read_excel(path, engine="openpyxl")

    # Rinomina colonne posizionali (Attendere giorno 15 dec per nuovo test)
    df.columns = [
        "time",
        "ticket",
        "symbol",
        "side",
        "entry_type",
        "volume",
        "price",
        "sl",
        "tp",
        "profit",
        "balance",
        "comment",
        "extra"
    ]

    # Teniamo solo righe con timestamp valido (trade)
    df = df[pd.to_datetime(df["time"], errors="coerce").notna()]

    df["time"] = pd.to_datetime(df["time"])

    return df.reset_index(drop=True)
