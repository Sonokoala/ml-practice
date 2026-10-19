import yfinance as yf
print(f"yfinance version: {yf.__version__}")

# テストとして AAPL（Apple Inc.）の情報を取得
aapl = yf.Ticker("AAPL")
print(aapl.info['longName'])