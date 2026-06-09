from app.macro.fred import get_latest_series_values


def _get_treasury_yield(series_id):
    values = get_latest_series_values(series_id, limit=5)

    if not values:
        return None

    current = values[0]
    previous = values[1] if len(values) > 1 else None

    change = None

    if previous:
        change = round(
            current["value"] - previous["value"],
            2
        )

    return {
        "yield": current["value"],
        "date": current["date"],
        "previous_yield": previous["value"] if previous else None,
        "previous_date": previous["date"] if previous else None,
        "change": change
    }


def get_us2y():
    return _get_treasury_yield("DGS2")


def get_us10y():
    return _get_treasury_yield("DGS10")


def get_us20y():
    return _get_treasury_yield("DGS20")


def get_yield_curve():
    us2y = get_us2y()
    us10y = get_us10y()

    if not us2y or not us10y:
        return None

    spread = round(
        us10y["yield"] - us2y["yield"],
        2
    )

    return {
        "2y": us2y["yield"],
        "10y": us10y["yield"],
        "spread": spread
    }