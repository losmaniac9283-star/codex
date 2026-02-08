# Stocks Dashboard for Top Companies

A simple full-stack app:

- **Backend**: Flask API (`/api/companies`) that pulls Yahoo Finance data via `yfinance` and computes 200-week SMA + diff %.
- **Frontend**: React table with search and sortable diff column.

## Prerequisites

- Python 3.10+
- Node.js 18+ and npm
- Internet access (the backend fetches market data from Yahoo)

---

## 1) Run the backend (Terminal A)

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python server.py
```

Backend starts at:

- `http://localhost:5000`
- API endpoint: `http://localhost:5000/api/companies`

Quick check (in another shell):

```bash
curl http://localhost:5000/api/companies
```

---

## 2) Run the frontend (Terminal B)

```bash
cd frontend
npm install
npm start
```

Frontend starts at:

- `http://localhost:3000`

The UI fetches from `http://localhost:5000/api/companies`.

---

## Common issues

- **`npm install` fails with 403**:
  - Check your npm registry config:
    ```bash
    npm config get registry
    ```
  - It should usually be:
    ```bash
    https://registry.npmjs.org/
    ```
  - If it is different and unintentionally set, reset it:
    ```bash
    npm config set registry https://registry.npmjs.org/
    ```

- **Frontend loads but no data appears**:
  - Ensure backend is running on port `5000`.
  - Open `http://localhost:5000/api/companies` directly in the browser to confirm JSON is returned.

- **Slow response**:
  - This is expected when querying many tickers. Add caching/batching for production-scale lists.
