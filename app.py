from flask import Flask, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def get_weather():
    location = request.args.get('location')
    if not location:
        return jsonify({'error': 'Location is required'}), 400
    
    api_key = 'def7c2879e42feca522e14bb6096e78c'  # Replace with your actual API key
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=imperial'
    response = requests.get(weather_url)
    
    if response.status_code == 200:
        data = response.json()
        weather_details = {
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'weather_description': data['weather'][0]['description'],
            'date': datetime.now().strftime('%Y-%m-%d'),
            'time': datetime.now().strftime("%H:%M:%S")
        }
        return jsonify(weather_details)
    else:
        return jsonify({'error': 'Failed to fetch weather data'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
