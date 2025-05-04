# Alpaca API Wrapper

A Flask-based API that connects to Alpaca Markets and provides AAPL price data across multiple timeframes.  
This project is built for integration with ChatGPT Actions.

---

## 🚀 Endpoints

| Endpoint        | Description            |
|-----------------|-----------------------|
| /aapl/10min    | AAPL 10-minute chart  |
| /aapl/1hour    | AAPL 1-hour chart     |
| /aapl/4hour    | AAPL 4-hour chart     |
| /aapl/1day     | AAPL 1-day chart      |
| /aapl/1week    | AAPL 1-week chart     |

---

## ⚙ Setup (local development)

1. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

2. Run the API:
    ```
    python alpaca_api_wrapper.py
    ```

3. Access locally:
    ```
    http://localhost:5000/aapl/10min
    ```

---

## 🌐 Deployment (Render)

1. Connect this repo to Render.com → New Web Service.
2. Build Command:
    ```
    pip install -r requirements.txt
    ```
3. Start Command:
    ```
    python alpaca_api_wrapper.py
    ```
4. Set environment variables:
    - API_KEY
    - API_SECRET
    - BASE_URL (`https://paper-api.alpaca.markets`)

---

## 🔗 OpenAPI Schema (for ChatGPT)

Use this raw schema link in ChatGPT → Actions → Add Action → Schema URL:

