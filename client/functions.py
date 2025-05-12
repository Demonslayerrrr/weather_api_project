from requests import get, post
from datetime import datetime

def post_function(lat,long,url, backedend_url):
    params = {
            "latitude": lat,
            "longitude": long,
            "hourly": "temperature_2m,wind_speed_10m,relative_humidity_2m"
    }


    response = get(url,params = params).json()["hourly"]


    data = {}
    for time_date,temp, w_speed, humidity in zip(response["time"],response["temperature_2m"], response["wind_speed_10m"], response["relative_humidity_2m"]):
        time_date = datetime.fromisoformat(time_date)
        if str(time_date.date()) not in data:
           data[str(time_date.date())] = {} 
             
        data[str(time_date.date())][str(time_date.time())] = { 
                "temperature": temp,
                "wind_speed": w_speed,
                "humidity": humidity
            }


    post(f"{backedend_url}/create_data",json=data)
     
def get_function(date,time, backend_url):
    response = get(f"{backend_url}/get_data?date={date}&time={time}")
    if response.status_code == 200:
        print(response.json())
    else:
        return None
