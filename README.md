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
9. To see the forecast on future days, open a web browser and navigate to ```http://127.0.0.1:5000/weather?location=YOUR_LOCATION&days=NUMBER_OF_DAYS``` replacing 'YOUR_LOCATION' with your desired location and 'NUMBER_OF_DAYS' with the number of days you wish to see.  
- For example: http://127.0.0.1:5000/weather?location=London would output the weather in London.
- http://127.0.0.1:5000/weather?location=London&days=5 would output the weather in London for the following five days.

## How to Request Data
- Endpoint: `/weather`
- Method: `GET`
- Query Parameters:
    - `location`: Name of the location (e.g., San Francisco)
    - `days`: Number of days to forecast (e.g., 5)

### Example Request
```python
import requests

url = 'http://127.0.0.1:5000/weather'
params = {
    'location': 'San Francisco',
    'days': 5  # Number of days to forecast
}
response = requests.get(url, params=params)
print(response.json())
```

### Output Format
```
{
  "current_weather": {
    "date": "2024-08-06",
    "humidity": 90,
    "location": "San Francisco",
    "temperature": 55.26,
    "time": "03:19:38",
    "weather_description": "broken clouds",
    "wind_speed": 8.05
  },
  "forecast": {
    "Tuesday": {
      "date": "2024-08-06",
      "humidity": 61,
      "location": "San Francisco",
      "temperature": 65.98,
      "weather_description": "few clouds",
      "wind_speed": 10.54
    }
  }
}
```

### Output Format For Multiple Days
```
{
  "current_weather": {
    "date": "2024-08-06",
    "humidity": 90,
    "location": "San Francisco",
    "temperature": 55.26,
    "time": "03:20:13",
    "weather_description": "broken clouds",
    "wind_speed": 8.05
  },
  "forecast": {
    "Friday": {
      "date": "2024-08-09",
      "humidity": 71,
      "location": "San Francisco",
      "temperature": 62.55,
      "weather_description": "scattered clouds",
      "wind_speed": 13.58
    },
    "Saturday": {
      "date": "2024-08-10",
      "humidity": 72,
      "location": "San Francisco",
      "temperature": 62.76,
      "weather_description": "few clouds",
      "wind_speed": 13.62
    },
    "Thursday": {
      "date": "2024-08-08",
      "humidity": 76,
      "location": "San Francisco",
      "temperature": 60.87,
      "weather_description": "few clouds",
      "wind_speed": 14.94
    },
    "Tuesday": {
      "date": "2024-08-06",
      "humidity": 61,
      "location": "San Francisco",
      "temperature": 65.98,
      "weather_description": "few clouds",
      "wind_speed": 10.54
    },
    "Wednesday": {
      "date": "2024-08-07",
      "humidity": 66,
      "location": "San Francisco",
      "temperature": 64.56,
      "weather_description": "few clouds",
      "wind_speed": 15.55
    }
  }
}
```

![UML Diagram (1)](https://github.com/user-attachments/assets/d949f865-9161-4e10-8b53-f2c43654bbec)

1. **For which teammate did you implement “Microservice A”?**
Muhammad Akbar


2. **What is the current status of the microservice? Hopefully, it’s done!**
The current status of the microservice is done. There might be changes made accordingly to suffice the main program.


3. **If the microservice isn’t done, which parts aren’t done and when will they be done?**
There might be changes made accordingly to suffice the main program. If there are any changes, then they will be done as soon as possible.


4. **How is your teammate going to access your microservice? Should they get your code from GitHub? Should they run your code locally? Is your microservice hosted somewhere? Etc.**
Clone the repository from GitHub and run the Flask app locally. Ensure you have the necessary dependencies installed.


5. **If your teammate cannot access/call YOUR microservice, what should they do? Can you be available to help them? What’s your availability?**
If my teammate cannot access call my microservice, then they should contact me immediately. I will be available to help them whenever I am not at work. My work schedule is Monday - Friday from 10 am to 9 pm (PST), including commute time. Otherwise, my availability is open.   


6. **If your teammate cannot access/call your microservice, by when do they need to tell you?**
If my teammate cannot access call my microservice, then they should contact me immediately. 


7. **Is there anything else your teammate needs to know? Anything you’re worried about? Any assumptions you’re making? Any other mitigations / backup plans you want to mention or want to discuss with your teammate?**
If the microservice does not work or there needs to be any changes within the microservice, please let me know and I will accommodate. Ensure you have an API key for OpenWeather(or use the one I provided) and update app.py accordingly. If you face any issues, feel free to reach out.


