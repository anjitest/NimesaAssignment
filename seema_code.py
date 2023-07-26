import requests

input_text = """Please enter any one of the option given below.
1. Get weather
2. Get Wind Speed
3. Get Pressure
0. Exit
"""

URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
response = requests.get(URL)
weather_response_data = response.json()

weather_data_of_given_date = {}
while True:
    # Accepts User input for weather data.
    user_option = input(input_text)

    # Edge case to handle the scenario where user passes string to input option
    if user_option.isalpha():
        print("Please enter valid input from the above options.\n")
        continue

    if int(user_option) in [1, 2, 3]:
        date = int(input("Please enter date in valid format to get weather data: "))

        # Iterating through the data to get the data which matches user input date.
        for row in weather_response_data['list']:
            if row['dt'] == date:
                weather_data_of_given_date = row

        # Conditional check on the user input for weather data.
        if int(user_option) == 1:
            temp = weather_data_of_given_date['main']['temp']
            print(f"Temperature of the given input date is: ", temp)
        elif int(user_option) == 2:
            wind_speed = weather_data_of_given_date['wind']['speed']
            print(f"Wind speed of the given input date is: ", wind_speed)
        else:
            pressure = weather_data_of_given_date['main']['pressure']
            print(f"Pressure of the given input date is: ", pressure)
    elif int(user_option) == 0:
        print("User exit the program by pressing `0`")
        break

