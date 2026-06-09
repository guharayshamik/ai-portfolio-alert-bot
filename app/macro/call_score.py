def calculate_call_buying_score(
    vixy,
    us2y,
    us10y,
    curve,
    dxy,
    crude,
    hyg,
    jnk,
    nearest_earnings=None,
):
    score = 50
    reasons = []

    # Volatility
    if vixy and vixy.get("change_pct") is not None:
        if vixy["change_pct"] <= -3:
            score += 10
            reasons.append("✓ VIX falling")
        elif vixy["change_pct"] >= 10:
            score -= 20
            reasons.append("✗ VIX spike")
        elif vixy["change_pct"] >= 5:
            score -= 15
            reasons.append("✗ VIX rising")
        elif vixy["change_pct"] >= 3:
            score -= 8
            reasons.append("✗ VIX watch")

    # Yield curve
    if curve and curve.get("spread") is not None:
        if curve["spread"] > 0:
            score += 10
            reasons.append("✓ Yield curve positive")
        else:
            score -= 15
            reasons.append("✗ Yield curve inverted")

    # 10Y Treasury
    if us10y and us10y.get("yield") is not None:
        us10y_yield = us10y["yield"]
        us10y_change = us10y.get("change")

        if us10y_yield >= 4.70:
            score -= 20
            reasons.append("✗ 10Y yield very high")
        elif us10y_yield >= 4.50:
            score -= 10
            reasons.append("✗ 10Y yield watch")
        elif us10y_yield < 4.30:
            score += 5
            reasons.append("✓ 10Y supportive")

        if us10y_change is not None:
            if us10y_change >= 0.10:
                score -= 10
                reasons.append("✗ 10Y rising fast")
            elif us10y_change <= -0.07:
                score += 5
                reasons.append("✓ 10Y falling")

    # 2Y Treasury / Fed expectations
    if us2y and us2y.get("yield") is not None:
        us2y_yield = us2y["yield"]
        us2y_change = us2y.get("change")

        if us2y_yield >= 4.50:
            score -= 10
            reasons.append("✗ 2Y yield elevated")

        if us2y_change is not None:
            if us2y_change >= 0.10:
                score -= 10
                reasons.append("✗ 2Y rising fast")
            elif us2y_change <= -0.07:
                score += 5
                reasons.append("✓ 2Y falling")

    # Dollar
    if dxy and dxy.get("price") is not None:
        if dxy["price"] >= 104:
            score -= 10
            reasons.append("✗ Strong dollar")
        elif dxy.get("change_pct") is not None and dxy["change_pct"] <= -0.5:
            score += 5
            reasons.append("✓ Dollar easing")

    # Crude oil
    if crude and crude.get("price") is not None:
        if crude["price"] >= 95:
            score -= 15
            reasons.append("✗ Crude very elevated")
        elif crude["price"] >= 90:
            score -= 10
            reasons.append("✗ Crude elevated")
        elif crude.get("change_pct") is not None and crude["change_pct"] <= -2:
            score += 5
            reasons.append("✓ Crude easing")

    # Credit
    if hyg is not None:
        if hyg > 0:
            score += 5
            reasons.append("✓ Credit healthy")
        elif hyg <= -1:
            score -= 10
            reasons.append("✗ HYG weak")

    if jnk is not None:
        if jnk > 0:
            score += 5
            reasons.append("✓ Junk bonds healthy")
        elif jnk <= -1:
            score -= 10
            reasons.append("✗ JNK weak")
    
    # Earnings penalty
    if nearest_earnings:
        days_left = nearest_earnings["days_left"]
        symbol = nearest_earnings["symbol"]

        if days_left <= 1:
            score -= 30
            reasons.append(f"✗ {symbol} earnings tomorrow")

        elif days_left <= 3:
            score -= 20
            reasons.append(f"✗ {symbol} earnings this week")

        elif days_left <= 7:
            score -= 10
            reasons.append(f"✗ {symbol} earnings approaching")

    score = max(0, min(100, score))

    return score, reasons


def call_buying_label(score):
    if score >= 75:
        return "🚀 Aggressive"
    if score >= 60:
        return "✅ Okay to add"
    if score >= 40:
        return "🟡 Small size only"
    return "🔴 Avoid new calls"


def build_call_buying_report(
    vixy,
    us2y,
    us10y,
    curve,
    dxy,
    crude,
    hyg,
    jnk,
    nearest_earnings=None,
):
    score, reasons = calculate_call_buying_score(
        vixy,
        us2y,
        us10y,
        curve,
        dxy,
        crude,
        hyg,
        jnk,
        nearest_earnings,
    )

    

    label = call_buying_label(score)
    reason_text = "\n".join(reasons) if reasons else "No strong drivers detected."

    return f"""🧠 Call Buying Score

Score: {score}/100

Bias:
{label}

Drivers:
{reason_text}
"""
