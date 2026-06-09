from app.market_data import get_quote

def get_vix():
    """
    Finnhub free plan does not support ^VIX directly.
    Use VIXY as a volatility proxy.
    """
    q = get_quote("VIXY")

    current = q.get("c")
    change_pct = q.get("dp")

    if not current:
        return None

    return {
        "symbol": "VIXY",
        "price": float(current),
        "change_pct": float(change_pct) if change_pct is not None else None
    }
