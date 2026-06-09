import requests
from app.config import FRED_API_KEY

FRED_OBSERVATIONS_URL = "https://api.stlouisfed.org/fred/series/observations"


def get_latest_series_value(series_id):
    values = get_latest_series_values(series_id, limit=1)

    if not values:
        return None

    return values[0]["value"]


def get_latest_series_values(series_id, limit=2):
    try:
        if not FRED_API_KEY:
            raise ValueError("FRED_API_KEY is missing")

        params = {
            "series_id": series_id,
            "api_key": FRED_API_KEY,
            "file_type": "json",
            "sort_order": "desc",
            "limit": limit,
        }

        response = requests.get(
            FRED_OBSERVATIONS_URL,
            params=params,
            timeout=15
        )

        response.raise_for_status()

        data = response.json()
        observations = data.get("observations", [])

        values = []

        for item in observations:
            value = item.get("value")
            date = item.get("date")

            if not value or value == ".":
                continue

            values.append({
                "date": date,
                "value": float(value)
            })

        return values

    except requests.exceptions.HTTPError as e:
        status = e.response.status_code if e.response else "Unknown"
        print(f"FRED error ({series_id}): HTTP {status}")
        return []

    except requests.exceptions.Timeout:
        print(f"FRED error ({series_id}): Timeout")
        return []

    except requests.exceptions.SSLError:
        print(f"FRED error ({series_id}): SSL certificate error")
        return []

    except requests.exceptions.RequestException:
        print(f"FRED error ({series_id}): Network error")
        return []

    except Exception as e:
        print(f"FRED error ({series_id}): {type(e).__name__}")
        return []
