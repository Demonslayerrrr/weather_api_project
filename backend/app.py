from flask import Flask, jsonify, request
from http import HTTPStatus
from controller import WeatherController
from repository import WeatherRepository
from pydantic import ValidationError

app = Flask(__name__)
repository = WeatherRepository()
controller = WeatherController(repository)

@app.post('/create_data')
def create_data():
    try:
        data = request.get_json()
        print(data)
        controller.create_data(data)
        return jsonify({"message": "Data created"}), HTTPStatus.CREATED
    except ValidationError as e:
        return jsonify({"message": str(e)}), HTTPStatus.UNPROCESSABLE_ENTITY

@app.get('/get_data')
def get_data():
    try:
        date = request.args.get('date')
        time = request.args.get('time')
        
        if not date or not time:
            return jsonify({"message": "Missing 'date' or 'time' parameter"}), HTTPStatus.BAD_REQUEST

        data = controller.get_data(date, time)
        return jsonify(data.model_dump()), HTTPStatus.OK    
    except Exception as e:
        return jsonify({"message": str(e)}), HTTPStatus.NOT_FOUND


if __name__ == '__main__':
    app.run(debug=True)

