from weather_client import get_current_weather


def main():
    print("Weather Monitoring Platform")
    print("---------------------------")

    try:
        weather = get_current_weather(
            latitude=23.588,
            longitude=58.383,
        )

        print(f"Observation Time: {weather['observation_time']}")
        print(f"Temperature: {weather['temperature']} °C")
        print(f"Humidity: {weather['humidity']} %")
        print(f"Pressure: {weather['pressure']} hPa")
        print(f"Wind Speed: {weather['wind_speed']} km/h")
        print(f"Wind Direction: {weather['wind_direction']}°")

    except RuntimeError as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()