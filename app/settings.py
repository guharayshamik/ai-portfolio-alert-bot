# Central project settings.
# Do not put secrets/API keys here.

PORTFOLIO_SCAN_SECONDS = 300
SLOW_SCAN_SECONDS = 3600
HOURLY_RANKING_SECONDS = 3600
MACRO_SCAN_SECONDS = 900

# Main loop sleep interval.
# This is only how often the bot wakes up to check whether a scan is due.
BOT_LOOP_SLEEP_SECONDS = 60

# Alert thresholds
VIX_WATCH_LEVEL = 18
VIX_RISK_LEVEL = 22
VIX_PANIC_LEVEL = 30

TLT_MOVE_ALERT_THRESHOLD = 1.0
MATERIAL_RISK_SCORE_CHANGE = 15
PORTFOLIO_DROP_ALERT = -3.0
