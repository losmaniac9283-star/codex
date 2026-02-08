from flask import Flask, jsonify
from flask_cors import CORS
import yfinance as yf

app = Flask(__name__)
CORS(app)  # allow cross-origin requests from the React frontend

# In practice, populate this list with ~1000 tickers of largest companies.
# This sample list keeps the demo fast and easy to run locally.
COMPANIES = [
    {"name": "Apple Inc.", "ticker": "AAPL"},
    {"name": "Microsoft Corp.", "ticker": "MSFT"},
    {"name": "Alphabet Inc.", "ticker": "GOOGL"},
    {"name": "Amazon.com Inc.", "ticker": "AMZN"},
    {"name": "NVIDIA Corp.", "ticker": "NVDA"},
    {"name": "Tesla Inc.", "ticker": "TSLA"},
    {"name": "Meta Platforms", "ticker": "META"},
    {"name": "Berkshire Hathaway", "ticker": "BRK-B"},
    {"name": "Taiwan Semiconductor", "ticker": "2330.TW"},
    {"name": "Samsung Electronics", "ticker": "005930.KS"},
]


@app.route('/api/companies')
def get_companies_data():
    """
    For each company, fetch current price and weekly data to compute the 200-week SMA.
    Returns JSON list of {name, ticker, price, sma200, diff}.
    """
    results = []

    for company in COMPANIES:
        ticker_symbol = company["ticker"]
        try:
            ticker = yf.Ticker(ticker_symbol)

            # Fetch enough weekly history to calculate the 200-week SMA.
            hist = ticker.history(period="210wk", interval="1wk")
            if hist is None or hist.empty:
                continue

            sma = hist['Close'].rolling(window=200).mean().iloc[-1]
            if sma != sma:  # NaN check
                continue

            # Current price from latest daily close.
            today_data = ticker.history(period="1d")
            if today_data is None or today_data.empty:
                continue

            price = today_data['Close'].iloc[-1]
            diff = (price - sma) / sma * 100 if sma != 0 else 0

            results.append(
                {
                    "name": company["name"],
                    "ticker": ticker_symbol,
                    "price": round(float(price), 2),
                    "sma200": round(float(sma), 2),
                    "diff": round(float(diff), 2),
                }
            )
        except Exception as exc:  # Skip bad/unsupported tickers and continue.
            print(f"Error fetching {ticker_symbol}: {exc}")

    return jsonify(results)


if __name__ == '__main__':
    # Flask development server: http://localhost:5000
    app.run(debug=True)
