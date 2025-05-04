from flask import Flask, jsonify
from alpaca_trade_api.rest import REST, TimeFrame
import pandas as pd
import os

app = Flask(__name__)

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
BASE_URL = os.getenv('BASE_URL')

api = REST(API_KEY, API_SECRET, BASE_URL)

@app.route('/aapl/10min')
def get_10min():
    bars = api.get_bars('AAPL', TimeFrame.Minute, limit=1000).df
    return jsonify(bars.reset_index().to_dict(orient='records'))

@app.route('/aapl/1hour')
def get_1hour():
    bars = api.get_bars('AAPL', TimeFrame.Hour, limit=1000).df
    return jsonify(bars.reset_index().to_dict(orient='records'))

@app.route('/aapl/4hour')
def get_4hour():
    bars = api.get_bars('AAPL', TimeFrame.Hour, limit=1000).df
    bars_resampled = bars[['close']].resample('4H').ohlc()
    return jsonify(bars_resampled.reset_index().to_dict(orient='records'))

@app.route('/aapl/1day')
def get_1day():
    bars = api.get_bars('AAPL', TimeFrame.Day, limit=2000).df
    return jsonify(bars.reset_index().to_dict(orient='records'))

@app.route('/aapl/1week')
def get_1week():
    bars = api.get_bars('AAPL', TimeFrame.Day, limit=2000).df
    bars_resampled = bars[['close']].resample('W').ohlc()
    return jsonify(bars_resampled.reset_index().to_dict(orient='records'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
