import requests


BASE_URL = "https://api.open-meteo.com/v1/forecast"


def validate_coordinates(
    latitude: float,
    longitude: float,
) -> None:
    if not -90 <= latitude <= 90:
        raise ValueError(
            "Latitude must be between -90 and 90."
        )

    if not -180 <= longitude <= 180:
        raise ValueError(
            "Longitude must be between -180 and 180."
        )


def get_current_weather(
    latitude: float,
    longitude: float,
) -> dict:

    validate_coordinates(latitude, longitude)

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": (
            "temperature_2m,"
            "relative_humidity_2m,"
            "surface_pressure,"
            "wind_speed_10m,"
            "wind_direction_10m"
        ),
    }

    try:
        response = requests.get(
            BASE_URL,
            params=params,
            timeout=10,
        )

        response.raise_for_status()

        data = response.json()
        current = data["current"]

        return {
            "observation_time": current["time"],
            "temperature": current["temperature_2m"],
            "humidity": current["relative_humidity_2m"],
            "pressure": current["surface_pressure"],
            "wind_speed": current["wind_speed_10m"],
            "wind_direction": current["wind_direction_10m"],
        }

    except requests.exceptions.Timeout as exc:
        raise RuntimeError(
            "Weather API request timed out."
        ) from exc

    except requests.exceptions.ConnectionError as exc:
        raise RuntimeError(
            "Could not connect to the weather API."
        ) from exc

    except requests.exceptions.HTTPError as exc:
        raise RuntimeError(
            "Weather API returned an HTTP error."
        ) from exc

    except requests.exceptions.RequestException as exc:
        raise RuntimeError(
            "Weather API request failed."
        ) from exc