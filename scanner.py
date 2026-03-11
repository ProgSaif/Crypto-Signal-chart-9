import requests
import pandas as pd


def get_klines(symbol, interval="15m", limit=150):

    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"

    data = requests.get(url).json()

    df = pd.DataFrame(data)

    df = df[[0,1,2,3,4,5]]

    df.columns = ["time","open","high","low","close","volume"]

    df["close"] = df["close"].astype(float)
    df["volume"] = df["volume"].astype(float)

    return df
