# Stocks Dashboard for Top Companies

This project provides:

- A Flask backend that fetches stock data with `yfinance`, calculates each company's 200-week SMA, and returns JSON.
- A React frontend that displays a searchable, sortable table of company price vs SMA distance.

## Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python server.py
```

API endpoint: `http://localhost:5000/api/companies`

## Frontend

```bash
cd frontend
npm install
npm start
```

App URL: `http://localhost:3000`

The frontend reads data from `http://localhost:5000/api/companies`.
