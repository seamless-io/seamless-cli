import yfinance as yf

tickers = [
    yf.Ticker("AAPL"),
    # ................
    # ^^ add tickers of companies you want to follow here
    # you can find a ticker from a company name here https://www.marketwatch.com/tools/quotes/lookup.asp
]


# By default Seamless Cloud will execute the function `main` in the file `function.py`
# You can override this behaviour by using --entrypoint flag
def main():
    for ticker in tickers:
        print(f"Company: {ticker.info['longName']}")
        print(f"Stock Price: {ticker.info['regularMarketPrice']}")
        print("Latest 3 recommendations:")
        print(ticker.recommendations.iloc[-3:])
