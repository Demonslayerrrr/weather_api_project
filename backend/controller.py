from model import Model, Values
from repository import WeatherRepository
from datetime import datetime

class WeatherController:
    def __init__(self, repository: WeatherRepository) -> None:
        self.repository = repository
    
    def create_data(self, data:dict)->None:
        for time_key, values_v in data.items():
            model = Model(time=datetime.fromisoformat(time_key),
                          values = Values(**values_v))
            self.repository.add(model)



