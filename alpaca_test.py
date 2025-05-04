import os
from dotenv import load_dotenv
from alpaca_trade_api.rest import REST

# Load API keys from .env file
load_dotenv()
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
BASE_URL = os.getenv('BASE_URL')

# Connect to Alpaca
api = REST(API_KEY, API_SECRET, BASE_URL)

# Check account status
account = api.get_account()
print(f'Account status: {account.status}')
