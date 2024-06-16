import argparse
import requests
from datetime import datetime as dt
from datetime import timedelta
import matplotlib.pyplot as plt
import textwrap

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent("""\
                                Weather forecast with OpenWeatherAPI
                                -----------------------------------------
                                    Saves image locally with forecast
                                    for city and date (today or tomorrow)
                                """)
)
parser.add_argument("--key",
                    "-K",
                    help="API Key for OpenWeatherAPI with activated One Call API 3.0. Details: https://openweathermap.org/api/one-call-3.",
                    type=str,
                    required=True)
parser.add_argument("--city",
                    "-C",
                    help="One or more cities for weatehr forecast. Usage: city_name,state_code,country_code with at least city required. Example: Bangkok,TH Tokyo New York,NY,US",
                    nargs="*",
                    required=True,
                    type=str)
parser.add_argument("--day",
                    "-D",
                    help="Day of weather forecast, either today or tomorrow.",
                    choices=["today", "tomorrow"],
                    default="today",
                    type=str)

args = parser.parse_args()

API_KEY = args.key
cities = args.city

def save_plot(hours, temps, feel_temps, pops, date, city):
    fig, ax1 = plt.subplots(figsize=(8, 5))

    # Plot the first line on the left y-axis
    ax1.plot(hours, temps, label='Temperature', marker='o', linestyle='-', color='b')
    ax1.plot(hours, feel_temps, label='Feels Like', marker='s', linestyle='--', color='r')

    # Set labels and titles
    ax1.set_xlabel('Hour')
    ax1.set_ylabel('Temperature ($^\circ$C)')
    ax1.set_title(f'Weather Forecast for {date} in {city}')

    # Create the second y-axis and plot the third line
    ax2 = ax1.twinx()
    ax2.plot(hours, pops, label='Probability of Precipitation', marker='^', linestyle='-.', color='g')
    ax2.set_ylabel('Percent, %')
    ax2.set_ylim(0, 100)

    # Combine the legends of both axes
    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines + lines2, labels + labels2, loc='upper left')

    plt.savefig(f'{city} - {date}.png')

if args.day == "today":
    DAY = (dt.today()).date()
else:
    DAY = (dt.today() + timedelta(days=1)).date()

for city in cities:
    geo_resp = requests.get(url=f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}").json()[0]
    predictions = "current,minutely,alerts"
    forecast_resp = requests.get(url=f"https://api.openweathermap.org/data/3.0/onecall?lat={geo_resp['lat']}&lon={geo_resp['lon']}&units=metric&exclude={predictions}&appid={API_KEY}").json()
    
    hourly = []
    for el in forecast_resp["hourly"]:
        if dt.fromtimestamp(el["dt"]).date() == DAY:
            hourly.append(el)
    
    days_forecast = forecast_resp["daily"][0] if args.day == "today" else forecast_resp["daily"][1]
    forecast = {
        "Date: ": DAY.strftime("%Y-%m-%d"),
        "Summary: ": days_forecast["summary"],
        "Max temperatur: ": days_forecast["temp"]["max"],
        "Min temperatur: ": days_forecast["temp"]["min"]
    }

    save_plot(
        hours=[dt.fromtimestamp(i['dt']).hour for i in hourly],
        temps=[i['temp'] for i in hourly],
        feel_temps=[i['feels_like'] for i in hourly],
        pops = [i['pop'] * 100 for i in hourly],
        date=DAY,
        city=city
    )
    
    print(city)
    print()
    for k, v in forecast.items():
        print(k, v, ".", sep="")
    print()