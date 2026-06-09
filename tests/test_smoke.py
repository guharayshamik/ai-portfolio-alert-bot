from app.macro.treasury import get_us2y, get_us10y, get_yield_curve
from app.macro.dashboard import build_macro_dashboard
from app.earnings import build_earnings_report, build_earnings_alert


def test_treasury_data():
    assert get_us2y() is not None
    assert get_us10y() is not None
    assert get_yield_curve() is not None


def test_macro_dashboard():
    msg, score = build_macro_dashboard()
    assert "Macro Dashboard" in msg
    assert isinstance(score, int)


def test_earnings_report_runs():
    report = build_earnings_report()
    assert report is None or "Upcoming Earnings" in report


def test_earnings_alert_runs():
    alerts = build_earnings_alert()
    assert isinstance(alerts, list)
