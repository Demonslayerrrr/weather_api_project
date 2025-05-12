from model import Model

class WeatherRepository:
    def __init__(self) -> None:
        self.data = []

    def add(self,model: Model) -> None:
        self.data.append(model)

    def get(self, date, time) -> Model:
        for model in self.data:
            if model.date == date and model.measurement.time == time:
                return model
        raise Exception("Data not found")
