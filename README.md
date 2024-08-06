# cs361_microservice

An Open Weather Map API to find the weather of a location based on location name.

## Prerequisite 
Set up the Flask App:
1. Install Flask and Requests: Ensure you have Python installed. Install Flask and requests using pip if you haven't already.
```
pip3 install Flask requests
```
   
2. Create a directory for your project and navigate to it. For example:
```
mkdir weather_api
cd weather_api
```

3. Install virtualenv to create an isolated development environment for the Flask microservice by running the command below:
```
pip3 install --user virtualenv
```

4. Create a virtual environment by running the following:
```
python3 -m venv ./venv
```

6. Finally, activate the virtual environment using one of the following commands based on your computer’s operating system:
```
source venv/bin/activate
```
## Setting up Weather API Key

An API key is already provided in app.py, but if you want to enter in your own weather api key, you can do so by signing up on https://openweathermap.org/ (or any other website that provides an api key)
- Navigate to 'My API Keys' under the profile settings
- Generate an api key
- Copy the api key and paste into the file app.py where it says **api_key = 'xxxx' # Replace xxxx with your actual API key** (Line 13)
  
## How To Use The Microservice
1. Download app.py and the test.py file.
2. Make sure that these files are placed in the root of your directory.
3. In the test.py file, edit the location to the location that is desired.
- In this example, 'San Francisco' was chosen
4. Open a terminal and navigate to the directory where your Flask application (app.py) is located.
- In this example, run the command ```cd weather_api``` since we created the directory weather_api (mkdir weather_api)
5. Use the following command to run the Flask server: ```python3 app.py```
6. In a new terminal window execute the test script: ```python3 test.py```
7. The test script should output the weather data for the specified location (e.g., San Francisco) if the microservice and API call are working correctly.
8. Open a web browser and navigate to ```http://127.0.0.1:5000/weather?location=``` to test if the server is responding to requests. You should see JSON data related to the weather for the specified location. **# After 'location=' enter the desired location.**
- For example: http://127.0.0.1:5000/weather?location=London would output the weather in London.

## How to Request Data
- Endpoint: `/weather`
- Method: `GET`
- Query Parameters:
    - `location`: Name of the location (e.g., San Francisco)

### Example Request
```python
import requests

url = 'http://127.0.0.1:5000/weather'
params = {'location': 'San Francisco'}
response = requests.get(url, params=params)
print(response.json())
```

### Output Format
```
{
  "date": "2024-08-05",
  "humidity": 91,
  "location": San Francisco,
  "temperature": 55.36,
  "time": "03:24:30",
  "weather_description": "overcast clouds",
  "wind_speed": 15.01
}
```
