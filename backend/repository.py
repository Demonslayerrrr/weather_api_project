from model import Model
from datetime import datetime

class WeatherRepository:
    def __init__(self) -> None:
        self.data = []

    def add(self,model: Model) -> None:
        self.data.append(model)

    def get(self,time) -> Model:
        time = datetime.fromisoformat(time)
        print(time)
        for model in self.data:
            if model.time == time:
                return model
        raise Exception("Data not found")
