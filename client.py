from dotenv import load_dotenv
from os import getenv
import requests
import argparse

load_dotenv()

lat = getenv("LAT")
long = getenv("LONG")
url = getenv("URL")

parser = argparse.ArgumentParser()

parser.add_argument("--lat")
parser.add_argument("--long")

args = parser.parse_args()

if args.__dict__["lat"] is not None and args.__dict__["long"] is not None:
    lat = args.__dict__["lat"]
    long = args.__dict__["long"]

params = {
        "latitude": lat,
        "longitude": long,
        "hourly": "temperature_2m,wind_speed_10m,relative_humidity_2m"
}


response = requests.get(url,params = params).json()["hourly"]


for time,temp, w_speed, humidity in zip(response["time"],response["temperature_2m"], response["wind_speed_10m"], response["relative_humidity_2m"]):
    print(f"{time} : {temp}, {w_speed}, {humidity}")

