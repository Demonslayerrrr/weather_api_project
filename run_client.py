from dotenv import load_dotenv
from os import getenv
import argparse
from client.functions import post_function, get_function

load_dotenv()

lat = getenv("LAT")
long = getenv("LONG")
url = getenv("URL")
backend_url = getenv("BACKEND_URL")

parser = argparse.ArgumentParser()


parser.add_argument("--post", action="store_true")
parser.add_argument("--get", action="store_true")

parser.add_argument("--lat", type=float, default=lat)
parser.add_argument("--long", type=float, default=long)

parser.add_argument("--date", type=str)
parser.add_argument("--time", type=str)

args = parser.parse_args()

if args.post:
    post_function(lat, long, url, backend_url)
elif args.get:
    get_function(args.date,args.time,backend_url)
else:
    print("No valid command provided. Use --post or --get.")
   
