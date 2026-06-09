import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def get_premarket_change(symbol):
    try:
        url = (
            f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
            "?range=1d&interval=1m&includePrePost=true"
        )

        response = requests.get(url, headers=HEADERS, timeout=15)
        response.raise_for_status()

        data = response.json()
        result = data["chart"]["result"][0]
        meta = result.get("meta", {})

        premarket_price = meta.get("preMarketPrice")
        previous_close = meta.get("previousClose")

        if premarket_price is None or previous_close is None:
            return None

        pct_change = ((premarket_price - previous_close) / previous_close) * 100

        return round(pct_change, 2)

    except Exception as e:
        print(f"Premarket fetch failed for {symbol}: {e}")
        return None


def collect_premarket_snapshot(symbols):
    snapshot = {}

    for symbol in symbols:
        snapshot[symbol] = get_premarket_change(symbol)

    return snapshot


def build_premarket_briefing(snapshot):
    lines = []
    weak_count = 0

    for symbol, pct in snapshot.items():
        if pct is None:
            lines.append(f"{symbol}: N/A")
            continue

        if pct < 0:
            weak_count += 1

        sign = "+" if pct > 0 else ""
        lines.append(f"{symbol}: {sign}{pct:.2f}%")

    if weak_count >= 4:
        interpretation = "🔴 Broad weakness detected before market open."
    elif weak_count >= 2:
        interpretation = "🟡 Mixed premarket conditions."
    else:
        interpretation = "🟢 Premarket conditions stable."

    return f"""📈 Premarket Briefing

{chr(10).join(lines)}

Interpretation:
{interpretation}
"""
