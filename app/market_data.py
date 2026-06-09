import time
import requests
from app.config import FINNHUB_API_KEY

REQUEST_DELAY_SECONDS = 1.2

def get_quote(symbol: str):
    if not FINNHUB_API_KEY:
        raise ValueError("FINNHUB_API_KEY is missing")

    url = "https://finnhub.io/api/v1/quote"
    params = {"symbol": symbol, "token": FINNHUB_API_KEY}

    try:
        response = requests.get(url, params=params, timeout=20)
    except requests.exceptions.SSLError:
        raise RuntimeError(f"SSL certificate error while fetching {symbol}. Possible VPN/proxy issue.")
    except requests.exceptions.Timeout:
        raise RuntimeError(f"Timeout while fetching {symbol}.")
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Network error while fetching {symbol}: {type(e).__name__}")

    if response.status_code == 429:
        raise RuntimeError(f"Rate limit hit while fetching {symbol}")

    if response.status_code == 401:
        raise RuntimeError(f"Unauthorized Finnhub request for {symbol}. Check API key.")

    response.raise_for_status()
    return response.json()

def get_daily_change_pct(symbol: str):
    time.sleep(REQUEST_DELAY_SECONDS)

    q = get_quote(symbol)

    current = q.get("c")
    previous = q.get("pc")

    if not current or not previous:
        return None

    return ((current - previous) / previous) * 100
