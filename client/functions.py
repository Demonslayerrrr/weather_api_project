from requests import get, post

def post_function(lat,long,url, backedend_url):
    params = {
            "latitude": lat,
            "longitude": long,
            "hourly": "temperature_2m,wind_speed_10m,relative_humidity_2m"
    }


    response = get(url,params = params).json()["hourly"]


    data = {}
    for time,temp, w_speed, humidity in zip(response["time"],response["temperature_2m"], response["wind_speed_10m"], response["relative_humidity_2m"]):
        data[time] = { 
            "temperature": temp,
            "wind_speed": w_speed,
            "humidity": humidity
        } 


    post(f"{backedend_url}/create_data",json=data)
     
def get_function(time, backend_url):
    if time is None:
        return None
    response = get(f"{backend_url}/get_data/{time}")
    if response.status_code == 200:
        return response.json()
    else:
        return None
