import os
import re
import time
import sys
sys.path.append('Weather')
import get_weather

if __name__ == '__main__':
	key_path = '/home/pi/APIKeys'
        city = 'Pasadena'
        state = 'CA'

	while True:
		# Get the API key for weather data
		api_key = get_weather.get_wunderground_key(key_path)
		
		# Get the weather data
		current_conditions = get_weather.get_current_conditions_wunderground(key_path, city, state)
		forecast = get_weather.get_forecast_wunderground(key_path, city, state)

		# Parse the weather data
		low_temp = get_weather.parse_forecast_wunderground(forecast, "low")
		high_temp = get_weather.parse_forecast_wunderground(forecast, "high")
		current_temp = get_weather.parse_current_conditions_wunderground(current_conditions, "temp_f")
		feelslike = get_weather.parse_current_conditions_wunderground(current_conditions, "feelslike")
		
	
		print(low_temp)
		print(high_temp)
		print(current_temp)
		print(feelslike)

		# Wait for 10 minutes
		time.sleep(600)
