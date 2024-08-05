import requests

def test_weather_api():
    url = 'http://127.0.0.1:5000/weather'
    params = {'location': 'San Francisco'}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        print('Weather data:', response.json())
    else:
        print('Failed to fetch weather data:', response.status_code)

if __name__ == '__main__':
    test_weather_api()