#from app.settings import TLT_MOVE_ALERT_THRESHOLD


def evaluate_vix(vix_data):
    if not vix_data:
        return ("UNKNOWN", None)

    price = vix_data["price"]
    change_pct = vix_data["change_pct"]

    if change_pct is None:
        return ("UNKNOWN", None)

    if change_pct >= 10:
        return (
            "HIGH",
            f"""🔴 Volatility Spike Alert

VIXY: {price:.2f}
Move Today: {change_pct:.2f}%

Interpretation:
Significant volatility expansion detected.

Portfolio Impact:
Negative for call options and high-growth names like MU, MRVL, COHR, NVDA and AMD."""
        )

    elif change_pct >= 5:
        return (
            "MEDIUM",
            f"""🟡 Volatility Rising

VIXY: {price:.2f}
Move Today: {change_pct:.2f}%

Interpretation:
Fear is building.
Monitor QQQ, SMH, SOXX and your options closely."""
        )

    elif change_pct >= 3:
        return (
            "WATCH",
            f"""🟡 Volatility Watch

VIXY: {price:.2f}
Move Today: {change_pct:.2f}%

Interpretation:
Early warning signal.
Risk appetite may be weakening."""
        )

    return ("LOW", None)


def evaluate_treasury(us10y_data):
    if us10y_data is None:
        return ("UNKNOWN", None)

    if isinstance(us10y_data, dict):
        yield_value = us10y_data.get("yield")
        change = us10y_data.get("change")
    else:
        yield_value = us10y_data
        change = None

    if yield_value is None:
        return ("UNKNOWN", None)

    change_text = "N/A" if change is None else f"{change:+.2f}%"

    if yield_value >= 4.70:
        return (
            "HIGH",
            f"""🔴 Treasury Yield Warning

US 10Y Yield: {yield_value:.2f}%
Daily Change: {change_text}

Interpretation:
10Y yield is elevated. This can pressure growth stocks, semiconductors and long-dated call options.

Portfolio Impact:
Negative for MU, MRVL, COHR, NVDA and AMD calls."""
        )

    if change is not None and change >= 0.10:
        return (
            "MEDIUM",
            f"""🟡 Treasury Yield Rising Fast

US 10Y Yield: {yield_value:.2f}%
Daily Change: {change_text}

Interpretation:
Yields are rising rapidly. Markets may be pricing fewer Fed cuts.

Portfolio Impact:
Can pressure Nasdaq, semiconductors and call options."""
        )

    if yield_value >= 4.50:
        return (
            "WATCH",
            f"""🟡 Treasury Yield Watch

US 10Y Yield: {yield_value:.2f}%
Daily Change: {change_text}

Interpretation:
Yields are approaching levels where growth stocks may become sensitive to Fed-rate expectations."""
        )

    return ("LOW", None)


def evaluate_yield_curve(curve_data):
    if not curve_data:
        return ("UNKNOWN", None)

    us2y = curve_data.get("2y")
    us10y = curve_data.get("10y")
    spread = curve_data.get("spread")

    if us2y is None or us10y is None or spread is None:
        return ("UNKNOWN", None)

    if spread < 0:
        return (
            "HIGH",
            f"""🔴 Yield Curve Warning

US 2Y Yield: {us2y:.2f}%
US 10Y Yield: {us10y:.2f}%
10Y - 2Y Spread: {spread:.2f}%

Interpretation:
Yield curve is inverted. This can signal tighter financial conditions and recession risk.

Portfolio Impact:
Be careful adding new call options in high-growth names like MU, MRVL, COHR, NVDA and AMD."""
        )

    if us2y >= 4.50:
        return (
            "MEDIUM",
            f"""🟡 Fed Rate Pressure Warning

US 2Y Yield: {us2y:.2f}%
US 10Y Yield: {us10y:.2f}%
10Y - 2Y Spread: {spread:.2f}%

Interpretation:
2Y yield is elevated. Market may be pricing fewer Fed cuts.

Portfolio Impact:
This can pressure Nasdaq, semiconductors and call options."""
        )

    if us10y >= 4.70:
        return (
            "MEDIUM",
            f"""🟡 Long-Term Yield Watch

US 2Y Yield: {us2y:.2f}%
US 10Y Yield: {us10y:.2f}%
10Y - 2Y Spread: {spread:.2f}%

Interpretation:
10Y yield is very elevated. Growth stock valuations may face pressure."""
        )

    return ("LOW", None)