from app.market_data import get_daily_change_pct
from app.watchlists import WATCHLISTS, STOCK_METADATA, FAST_SYMBOLS, SLOW_SYMBOLS

PORTFOLIO_DROP_ALERT = -3.0
GROUP_AVG_DROP_ALERT = -2.0
MATERIAL_RISK_SCORE_CHANGE = 15


def company_label(symbol):
    info = STOCK_METADATA.get(symbol)

    if info:
        return f"{symbol} ({info['name']})"

    for group in WATCHLISTS.values():
        if symbol in group["symbols"]:
            return f"{symbol} ({group['symbols'][symbol]})"

    return symbol


def format_pct(value):
    if value is None:
        return "N/A"
    return f"{value:.2f}%"


def collect_market_snapshot(symbols):
    snapshot = {}

    for symbol in symbols:
        try:
            snapshot[symbol] = get_daily_change_pct(symbol)
        except Exception as e:
            print(f"Could not fetch {symbol}: {str(e).split('token=')[0]}")
            snapshot[symbol] = None

    return snapshot


def group_average(symbols, snapshot):
    values = [
        snapshot.get(symbol)
        for symbol in symbols
        if snapshot.get(symbol) is not None
    ]

    if not values:
        return None

    return sum(values) / len(values)


def calculate_risk_score(snapshot):
    score = 0

    qqq = snapshot.get("QQQ")
    spy = snapshot.get("SPY")
    smh = snapshot.get("SMH")
    soxx = snapshot.get("SOXX")
    hyg = snapshot.get("HYG")
    jnk = snapshot.get("JNK")

    if qqq is not None and qqq <= -1:
        score += 15
    if spy is not None and spy <= -1:
        score += 10
    if smh is not None and smh <= -1.5:
        score += 20
    if soxx is not None and soxx <= -1.5:
        score += 20
    if hyg is not None and hyg <= -0.5:
        score += 10
    if jnk is not None and jnk <= -0.5:
        score += 10

    portfolio_symbols = ["MU", "MRVL", "COHR", "NVDA", "AMD", "ARM", "INTC"]
    weak_portfolio = [
        s for s in portfolio_symbols
        if snapshot.get(s) is not None and snapshot[s] <= -3
    ]

    if len(weak_portfolio) >= 2:
        score += 20

    if len(weak_portfolio) >= 4:
        score += 20

    return min(score, 100)


def risk_label(score):
    if score >= 70:
        return "HIGH"
    if score >= 40:
        return "MEDIUM"
    return "LOW"


def detect_portfolio_alerts(snapshot):
    alerts = []

    portfolio_symbols = ["MU", "MRVL", "COHR", "NVDA", "AMD", "ARM", "INTC"]

    smh = snapshot.get("SMH")
    soxx = snapshot.get("SOXX")
    qqq = snapshot.get("QQQ")

    sector_weak = (
        (smh is not None and smh <= -1.5)
        or (soxx is not None and soxx <= -1.5)
        or (qqq is not None and qqq <= -1.5)
    )

    for symbol in portfolio_symbols:
        pct = snapshot.get(symbol)

        if pct is None:
            continue

        threshold = STOCK_METADATA.get(symbol, {}).get("alert_threshold", PORTFOLIO_DROP_ALERT)

        if pct <= threshold:
            if sector_weak:
                reason = "This appears connected to broader semiconductor / Nasdaq weakness."
            else:
                reason = "This may be stock-specific because QQQ / SMH / SOXX are not confirming the drop."

            alerts.append(f"""🔴 Portfolio Stock Alert

{company_label(symbol)}: {format_pct(pct)}

{reason}

Sector Check:
{company_label('QQQ')}: {format_pct(qqq)}
{company_label('SMH')}: {format_pct(smh)}
{company_label('SOXX')}: {format_pct(soxx)}""")

    return alerts


def detect_industry_pressure(snapshot):
    alerts = {}
    
    for symbol, pct in snapshot.items():
        if pct is None:
            continue

        info = STOCK_METADATA.get(symbol)
        if not info:
            continue

        industry = info.get("industry", "Unknown")
        threshold = info.get("alert_threshold", -3)

        if pct <= threshold:
            alerts.setdefault(industry, []).append(symbol)

    messages = []

    for industry, symbols in alerts.items():
        if len(symbols) < 2:
            continue

        sector = STOCK_METADATA[symbols[0]].get("sector", "Unknown")

        weak_lines = [
            f"{company_label(symbol)}: {format_pct(snapshot.get(symbol))}"
            for symbol in symbols
        ]

        portfolio_hits = [
            symbol for symbol in symbols
            if STOCK_METADATA.get(symbol, {}).get("portfolio") is True
        ]

        if portfolio_hits:
            portfolio_line = "Portfolio Impact: " + ", ".join(company_label(s) for s in portfolio_hits)
        else:
            portfolio_line = "Portfolio Impact: No direct portfolio holding detected."

        messages.append(f"""🔴 {industry} Industry Weakness

{chr(10).join(weak_lines)}

Industry: {industry}
Sector: {sector}
{portfolio_line}

Interpretation:
This appears industry-specific, not just one isolated stock.""")

    return messages


def detect_sector_pressure(snapshot):
    sectors = {}

    for symbol, pct in snapshot.items():
        if pct is None:
            continue

        info = STOCK_METADATA.get(symbol)
        if not info:
            continue

        sector = info.get("sector", "Unknown")
        threshold = info.get("alert_threshold", -3)

        if pct <= threshold:
            sectors.setdefault(sector, []).append(symbol)

    messages = []

    for sector, symbols in sectors.items():
        if len(symbols) < 3:
            continue

        weak_lines = [
            f"{company_label(symbol)}: {format_pct(snapshot.get(symbol))}"
            for symbol in symbols
        ]

        portfolio_hits = [
            symbol for symbol in symbols
            if STOCK_METADATA.get(symbol, {}).get("portfolio") is True
        ]

        if portfolio_hits:
            portfolio_line = "Portfolio Impact: " + ", ".join(company_label(s) for s in portfolio_hits)
        else:
            portfolio_line = "Portfolio Impact: No direct portfolio holding detected."

        messages.append(f"""🔴 {sector} Sector Weakness

{chr(10).join(weak_lines)}

Sector: {sector}
{portfolio_line}

Interpretation:
This looks like broad sector weakness, not a single-company issue.""")

    return messages


def build_morning_briefing(snapshot):
    score = calculate_risk_score(snapshot)
    label = risk_label(score)

    key_lines = [
        f"{company_label('QQQ')}: {format_pct(snapshot.get('QQQ'))}",
        f"{company_label('SPY')}: {format_pct(snapshot.get('SPY'))}",
        f"{company_label('SMH')}: {format_pct(snapshot.get('SMH'))}",
        f"{company_label('SOXX')}: {format_pct(snapshot.get('SOXX'))}",
        f"{company_label('HYG')}: {format_pct(snapshot.get('HYG'))}",
        f"{company_label('JNK')}: {format_pct(snapshot.get('JNK'))}",
    ]

    portfolio_symbols = ["MU", "MRVL", "COHR", "NVDA", "AMD", "ARM", "INTC"]

    portfolio_lines = [
        f"{company_label(symbol)}: {format_pct(snapshot.get(symbol))}"
        for symbol in portfolio_symbols
    ]

    return f"""📊 Morning Market Briefing

Risk Score: {score}/100
Portfolio Risk: {label}

Market Signals:
{chr(10).join(key_lines)}

My Portfolio:
{chr(10).join(portfolio_lines)}

Interpretation:
{brief_interpretation(score)}""", score


def brief_interpretation(score):
    if score >= 70:
        return "🔴 High risk. Broad market / semiconductor pressure is active. Be careful with new call options."
    if score >= 40:
        return "🟡 Medium risk. Conditions are mixed. Watch whether weakness spreads."
    return "🟢 Low risk. No major portfolio-wide pressure detected yet."


def build_risk_change_alert(previous_score, current_score, snapshot):
    if current_score - previous_score < MATERIAL_RISK_SCORE_CHANGE:
        return None

    return f"""🔴 Risk Increased Materially

Previous Risk Score: {previous_score}/100
Current Risk Score: {current_score}/100
Portfolio Risk: {risk_label(current_score)}

Key Signals:
{company_label('QQQ')}: {format_pct(snapshot.get('QQQ'))}
{company_label('SMH')}: {format_pct(snapshot.get('SMH'))}
{company_label('SOXX')}: {format_pct(snapshot.get('SOXX'))}
{company_label('MU')}: {format_pct(snapshot.get('MU'))}
{company_label('MRVL')}: {format_pct(snapshot.get('MRVL'))}
{company_label('COHR')}: {format_pct(snapshot.get('COHR'))}

Interpretation:
Risk has worsened meaningfully. Check whether this is sector-wide semiconductor weakness or portfolio-specific damage."""


def build_hourly_portfolio_ranking(snapshot):
    portfolio_symbols = ["MU", "MRVL", "COHR", "NVDA", "AMD", "ARM", "INTC"]

    rows = [
        (symbol, snapshot.get(symbol))
        for symbol in portfolio_symbols
        if snapshot.get(symbol) is not None
    ]

    if not rows:
        return None

    rows.sort(key=lambda x: x[1], reverse=True)

    best = rows[:3]
    worst = rows[-3:]

    best_lines = [f"{company_label(s)}: {format_pct(p)}" for s, p in best]
    worst_lines = [f"{company_label(s)}: {format_pct(p)}" for s, p in worst]

    return f"""📊 Hourly Portfolio Ranking

Best Relative Performers:
{chr(10).join(best_lines)}

Worst Relative Performers:
{chr(10).join(worst_lines)}

Interpretation:
This shows which portfolio names are holding up better or worse versus your other holdings."""


def build_contextual_alerts(snapshot):
    alerts = []
    alerts.extend(detect_portfolio_alerts(snapshot))
    alerts.extend(detect_industry_pressure(snapshot))
    alerts.extend(detect_sector_pressure(snapshot))
    return alerts
