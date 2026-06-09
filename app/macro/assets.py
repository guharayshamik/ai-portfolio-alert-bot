import requests
from urllib.parse import quote

HEADERS = {"User-Agent": "Mozilla/5.0"}


def get_yahoo_asset(symbol):
    try:
        encoded = quote(symbol, safe="")
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{encoded}"

        response = requests.get(
            url,
            params={"range": "1d", "interval": "1m"},
            headers=HEADERS,
            timeout=15
        )
        response.raise_for_status()

        data = response.json()
        result = data["chart"]["result"][0]
        meta = result.get("meta", {})

        price = meta.get("regularMarketPrice")
        previous = meta.get("previousClose")

        if price is None or previous is None or previous == 0:
            return None

        change_pct = ((price - previous) / previous) * 100

        return {
            "symbol": symbol,
            "price": round(price, 2),
            "previous": round(previous, 2),
            "change_pct": round(change_pct, 2),
        }

    except Exception as e:
        print(f"Yahoo asset fetch failed for {symbol}: {e}")
        return None


def get_dxy():
    return get_yahoo_asset("DX-Y.NYB")


def get_crude_oil():
    return get_yahoo_asset("CL=F")
