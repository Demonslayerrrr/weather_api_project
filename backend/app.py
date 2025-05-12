from flask import Flask, jsonify, request
from http import HTTPStatus
from flask.views import MethodView
from controller import WeatherController
from repository import WeatherRepository
from pydantic import ValidationError

app = Flask(__name__)

repository = WeatherRepository()
controller = WeatherController(repository)

class CreateDataView(MethodView):
    def __init__(self, controller: WeatherController):
        self.controller = controller

    def post(self):
        try:
            data = request.get_json()
            print(data)
            self.controller.create_data(data)
            return jsonify({"message": "Data created"}), HTTPStatus.CREATED
        except ValidationError as e:
            return jsonify({"message": str(e)}), HTTPStatus.UNPROCESSABLE_ENTITY

class GetDataView(MethodView):
    def __init__(self, controller: WeatherController):
        self.controller = controller

    def get(self):
        try:
            date = request.args.get('date')
            time = request.args.get('time')
            
            if not date or not time:
                return jsonify({"message": "Missing 'date' or 'time' parameter"}), HTTPStatus.BAD_REQUEST

            data = self.controller.get_data(date, time)
            return jsonify(data.model_dump()), HTTPStatus.OK    
        except Exception as e:
            return jsonify({"message": str(e)}), HTTPStatus.NOT_FOUND

app.add_url_rule('/create_data', view_func=CreateDataView.as_view('create_data', controller=controller))
app.add_url_rule('/get_data', view_func=GetDataView.as_view('get_data', controller=controller))

if __name__ == '__main__':
    app.run(debug=True)

