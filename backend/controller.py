from model import Model,Measurement, Values
from repository import WeatherRepository

class WeatherController:
    def __init__(self, repository: WeatherRepository) -> None:
        self.repository = repository
    
    def create_data(self, data: dict) -> None:
        for date, measurement_dict in data.items():
            for time, values in measurement_dict.items():
                measurement = Measurement(time=time, values=Values(**values))
                model = Model(date=date, measurement=measurement)
                self.repository.add(model)


    def get_data(self,date,time)-> Model:
        return self.repository.get(date,time)


