import time
from datetime import date

from app.config import CHECK_INTERVAL_SECONDS
from app.settings import (
    PORTFOLIO_SCAN_SECONDS,
    SLOW_SCAN_SECONDS,
    HOURLY_RANKING_SECONDS,
    MACRO_SCAN_SECONDS,
    BOT_LOOP_SLEEP_SECONDS,
)
from app.telegram_alerts import send_alert
from app.watchlists import FAST_SYMBOLS, SLOW_SYMBOLS
from app.rules import (
    collect_market_snapshot,
    calculate_risk_score,
    build_morning_briefing,
    build_risk_change_alert,
    build_contextual_alerts,
    build_hourly_portfolio_ranking,
)
from app.earnings import (
    build_earnings_report,
    build_earnings_alert,
)

from app.macro.dashboard import build_macro_dashboard
from app.macro.vix import get_vix
from app.macro.treasury import (
    get_us10y,
    get_yield_curve,
)
from app.macro.rules import (
    evaluate_vix,
    evaluate_treasury,
    evaluate_yield_curve,
)


def main():
    send_alert("✅ Sam Ray Market Intelligence Bot started.")

    last_briefing_date = None
    last_portfolio_scan = 0
    last_slow_scan = 0
    last_hourly_ranking = 0
    last_macro_scan = 0

    previous_risk_score = None
    last_vix_alert = None
    last_yield_alert = None
    last_yield_curve_alert = None
    last_macro_dashboard_alert = None

    sent_alerts = set()
    latest_snapshot = {}

    while True:
        try:
            now = time.time()
            today = date.today()

            # Macro scan
            if now - last_macro_scan >= MACRO_SCAN_SECONDS:

                # VIX / volatility
                try:
                    vix = get_vix()
                    risk_level, msg = evaluate_vix(vix)

                    if msg and msg != last_vix_alert:
                        send_alert(msg)
                        last_vix_alert = msg

                except Exception as e:
                    print("VIX error:", e)

                # US 10Y Treasury
                try:
                    us10y = get_us10y()
                    risk_level, msg = evaluate_treasury(us10y)

                    if msg and msg != last_yield_alert:
                        send_alert(msg)
                        last_yield_alert = msg

                except Exception as e:
                    print("Treasury error:", e)

                # Yield curve
                try:
                    curve = get_yield_curve()
                    risk_level, msg = evaluate_yield_curve(curve)

                    if msg and msg != last_yield_curve_alert:
                        send_alert(msg)
                        last_yield_curve_alert = msg

                except Exception as e:
                    print("Yield curve error:", e)

                # Grouped macro dashboard
                try:
                    macro_msg, macro_score = build_macro_dashboard()

                    if macro_msg and macro_msg != last_macro_dashboard_alert:
                        send_alert(macro_msg)
                        last_macro_dashboard_alert = macro_msg

                except Exception as e:
                    print("Macro dashboard error:", e)

                last_macro_scan = now

            # Portfolio scan
            if now - last_portfolio_scan >= PORTFOLIO_SCAN_SECONDS:
                fast_snapshot = collect_market_snapshot(FAST_SYMBOLS)
                latest_snapshot.update(fast_snapshot)

                current_score = calculate_risk_score(latest_snapshot)

                # Morning briefing once per day
                if last_briefing_date != today:
                    briefing, score = build_morning_briefing(latest_snapshot)
                    send_alert(briefing)

                    earnings_report = build_earnings_report()
                    if earnings_report:
                        send_alert(earnings_report)

                    previous_risk_score = score
                    last_briefing_date = today
                    sent_alerts.clear()

                # Risk score material change alert
                if previous_risk_score is not None:
                    risk_alert = build_risk_change_alert(
                        previous_risk_score,
                        current_score,
                        latest_snapshot
                    )

                    if risk_alert:
                        send_alert(risk_alert)
                        previous_risk_score = current_score

                contextual_alerts = build_contextual_alerts(latest_snapshot)

                earnings_alerts = build_earnings_alert()
                contextual_alerts.extend(earnings_alerts)

                for alert in contextual_alerts:
                    if alert not in sent_alerts:
                        send_alert(alert)
                        sent_alerts.add(alert)

                last_portfolio_scan = now

            # Slow broader market scan
            if now - last_slow_scan >= SLOW_SCAN_SECONDS:
                slow_snapshot = collect_market_snapshot(SLOW_SYMBOLS)
                latest_snapshot.update(slow_snapshot)
                last_slow_scan = now

            # Hourly portfolio ranking
            if now - last_hourly_ranking >= HOURLY_RANKING_SECONDS:
                ranking = build_hourly_portfolio_ranking(latest_snapshot)

                if ranking:
                    send_alert(ranking)

                last_hourly_ranking = now

            time.sleep(BOT_LOOP_SLEEP_SECONDS)

        except KeyboardInterrupt:
            send_alert("🛑 Sam Ray Market Intelligence Bot stopped.")
            break

        except Exception as e:
            print("Error:", e)
            time.sleep(CHECK_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
