from model import Model

class WeatherRepository:
    def __init__(self) -> None:
        self.data = []

    def add(self,model: Model) -> None:
        self.data.append(model)

    def get(self,time) -> Model:
        pass
