from app.macro.vix import get_vix
from app.macro.treasury import get_us2y, get_us10y, get_yield_curve
from app.macro.assets import get_dxy, get_crude_oil
from app.market_data import get_daily_change_pct


def fmt_pct(value):
    if value is None:
        return "N/A"
    sign = "+" if value > 0 else ""
    return f"{sign}{value:.2f}%"


def fmt_yield(data):
    if not data:
        return "N/A"

    change = data.get("change")
    change_text = "N/A" if change is None else f"{change:+.2f}"

    return f"{data['yield']:.2f}% ({change_text})"


def calculate_macro_score(vixy, us2y, us10y, curve, dxy, crude, hyg, jnk):
    score = 0
    risk_drivers = []

    if vixy and vixy.get("change_pct") is not None:
        if vixy["change_pct"] >= 10:
            score += 25
            risk_drivers.append("VIXY spike")
        elif vixy["change_pct"] >= 5:
            score += 15
            risk_drivers.append("VIXY rising")
        elif vixy["change_pct"] >= 3:
            score += 8
            risk_drivers.append("VIXY watch")

    if us2y and us2y.get("yield") is not None:
        if us2y["yield"] >= 4.50:
            score += 20
            risk_drivers.append("2Y yield elevated")
        elif us2y["yield"] >= 4.25:
            score += 10
            risk_drivers.append("2Y yield watch")

    if us10y and us10y.get("yield") is not None:
        if us10y["yield"] >= 4.70:
            score += 25
            risk_drivers.append("10Y yield high")
        elif us10y["yield"] >= 4.50:
            score += 15
            risk_drivers.append("10Y yield watch")

    if curve and curve.get("spread") is not None:
        if curve["spread"] < 0:
            score += 15
            risk_drivers.append("Yield curve inverted")

    if dxy and dxy.get("price") is not None:
        if dxy["price"] >= 104:
            score += 15
            risk_drivers.append("Dollar strong")
        elif dxy["price"] >= 102:
            score += 8
            risk_drivers.append("Dollar watch")

    if crude and crude.get("price") is not None:
        if crude["price"] >= 95:
            score += 25
            risk_drivers.append("Crude oil very high")
        elif crude["price"] >= 90:
            score += 20
            risk_drivers.append("Crude oil elevated")
        elif crude["price"] >= 80:
            score += 10
            risk_drivers.append("Crude oil watch")

    if hyg is not None:
        if hyg <= -1:
            score += 15
            risk_drivers.append("HYG weak")
        elif hyg <= -0.5:
            score += 8
            risk_drivers.append("HYG watch")

    if jnk is not None:
        if jnk <= -1:
            score += 15
            risk_drivers.append("JNK weak")
        elif jnk <= -0.5:
            score += 8
            risk_drivers.append("JNK watch")

    return min(score, 100), risk_drivers


def macro_label(score):
    if score >= 70:
        return "HIGH"
    if score >= 40:
        return "MEDIUM"
    return "LOW"


def build_interpretation(label, risk_drivers):
    if label == "HIGH":
        return "🔴 Macro risk is high. Avoid aggressive new call buying unless there is a strong catalyst."

    if label == "MEDIUM":
        return "🟡 Mixed macro conditions. Add calls carefully and prefer smaller size."

    if risk_drivers:
        return (
            "🟡 Macro backdrop is mostly supportive, but watch: "
            + ", ".join(risk_drivers)
            + "."
        )

    return "🟢 Macro backdrop is not currently hostile to growth stocks."


def build_macro_dashboard():
    vixy = get_vix()
    us2y = get_us2y()
    us10y = get_us10y()
    curve = get_yield_curve()
    dxy = get_dxy()
    crude = get_crude_oil()

    try:
        hyg = get_daily_change_pct("HYG")
    except Exception:
        hyg = None

    try:
        jnk = get_daily_change_pct("JNK")
    except Exception:
        jnk = None

    score, risk_drivers = calculate_macro_score(
        vixy=vixy,
        us2y=us2y,
        us10y=us10y,
        curve=curve,
        dxy=dxy,
        crude=crude,
        hyg=hyg,
        jnk=jnk
    )

    label = macro_label(score)

    vixy_line = "N/A"
    if vixy:
        vixy_line = f"{vixy['price']:.2f} ({fmt_pct(vixy.get('change_pct'))})"

    dxy_line = "N/A"
    if dxy:
        dxy_line = f"{dxy['price']:.2f} ({fmt_pct(dxy.get('change_pct'))})"

    crude_line = "N/A"
    if crude:
        crude_line = f"${crude['price']:.2f} ({fmt_pct(crude.get('change_pct'))})"

    curve_line = "N/A"
    if curve:
        curve_line = f"{curve['spread']:+.2f}%"

    drivers_line = "None"
    if risk_drivers:
        drivers_line = ", ".join(risk_drivers)

    interpretation = build_interpretation(label, risk_drivers)

    message = f"""🌎 Macro Dashboard

Macro Risk Score: {score}/100
Macro Risk: {label}

Volatility:
VIXY: {vixy_line}

Rates:
US 2Y: {fmt_yield(us2y)}
US 10Y: {fmt_yield(us10y)}
10Y - 2Y Spread: {curve_line}

Dollar:
DXY: {dxy_line}

Energy:
WTI Crude: {crude_line}

Credit:
HYG: {fmt_pct(hyg)}
JNK: {fmt_pct(jnk)}

Risk Drivers:
{drivers_line}

Interpretation:
{interpretation}
"""

    return message, score
