import requests
from datetime import date, timedelta

from app.config import FINNHUB_API_KEY
from app.watchlists import EARNINGS_WATCHLIST, PORTFOLIO_SYMBOLS

EARNINGS_WATCHLIST = [
    "MU",
    "MRVL",
    "COHR",
    "NVDA",
    "AMD",
    "ARM",
    "INTC",
    "PANW",
    "CRWD",
    "ORCL"
]


def get_earnings_calendar(days=60):
    if not FINNHUB_API_KEY:
        print("Earnings error: FINNHUB_API_KEY is missing")
        return []

    start = date.today()
    end = start + timedelta(days=days)

    params = {
        "from": start.isoformat(),
        "to": end.isoformat(),
        "token": FINNHUB_API_KEY,
    }

    try:
        response = requests.get(
            "https://finnhub.io/api/v1/calendar/earnings",
            params=params,
            timeout=20
        )

        response.raise_for_status()
        data = response.json()

        return data.get("earningsCalendar", [])

    except requests.exceptions.HTTPError as e:
        status = e.response.status_code if e.response else "Unknown"
        print(f"Earnings error: HTTP {status}")
        return []

    except requests.exceptions.Timeout:
        print("Earnings error: Timeout")
        return []

    except requests.exceptions.SSLError:
        print("Earnings error: SSL certificate error")
        return []

    except requests.exceptions.RequestException:
        print("Earnings error: Network error")
        return []

    except Exception as e:
        print(f"Earnings error: {type(e).__name__}")
        return []


def get_watchlist_earnings(days=60):
    raw = get_earnings_calendar(days=days)
    watched = set(EARNINGS_WATCHLIST)

    results = []

    for item in raw:
        symbol = item.get("symbol")

        if symbol not in watched:
            continue

        earnings_date = item.get("date")

        if not earnings_date:
            continue

        try:
            earnings_day = date.fromisoformat(earnings_date)
            days_left = (earnings_day - date.today()).days
        except Exception:
            days_left = None

        results.append({
            "symbol": symbol,
            "date": earnings_date,
            "days_left": days_left,
            "hour": item.get("hour") or "TBD",
            "eps_estimate": item.get("epsEstimate"),
            "revenue_estimate": item.get("revenueEstimate"),
        })

    results.sort(
        key=lambda x: x["days_left"] if x["days_left"] is not None else 9999
    )

    return results


def build_earnings_report():
    #earnings = get_watchlist_earnings(days=120)
    earnings = get_watchlist_earnings(days=120)

    if not earnings:
        return None

    next_30 = []
    next_60 = []

    for item in earnings:
        hour = item["hour"]
        eps = item["eps_estimate"]

        eps_text = "N/A" if eps is None else f"{eps:.2f}"

        line = (
            f"{item['symbol']} - {item['date']} "
            f"({item['days_left']} days, {hour}, EPS est: {eps_text})"
        )

        if item["days_left"] is not None and item["days_left"] <= 30:
            next_30.append(line)
        else:
            next_60.append(line)

    message = "📅 Upcoming Earnings\n\n"

    if next_30:
        message += "Next 30 Days:\n"
        message += "\n".join(next_30)
        message += "\n\n"

    if next_60:
        message += "Next 31-120 Days:\n"
        message += "\n".join(next_60)

    return message.strip()


def build_earnings_alert():
    earnings = get_watchlist_earnings(days=14)
    alerts = []

    for item in earnings:
        days_left = item["days_left"]

        if days_left is None:
            continue

        if days_left <= 7:
            alerts.append(
                f"""🔴 Earnings Risk Alert

{item['symbol']} earnings in {days_left} days.
Date: {item['date']}
Time: {item['hour']}

Interpretation:
Be cautious adding large call positions immediately before earnings."""
            )

    return alerts
