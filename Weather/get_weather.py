#!/usr/bin/env python3

import sys
import os
import re
import requests

def parse_current_conditions_wunderground(json_data, value):
	# Initialize variables
	return_value = None	

	# Parse the data as needed
	if "temp" in value: return_value = json_data["current_observation"]["temp_f"]
	elif "weather" in value: return_value = json_data["current_observation"]["weather"]
	elif "humidity" in value: return_value = json_data["current_observation"]["relative_humidity"]
	elif "wind" in value: return_value = json_data["current_observation"]["wind_string"]
	elif "feelslike" in value: return_value = json_data["current_observation"]["feelslike_f"]
	
	return return_value

def get_current_conditions_wunderground(api_key, city, state):
	# Initialize the variables
	json_response = None	

	# Create the target url
	target_url = 'http://api.wunderground.com/api/' + api_key + '/conditions/q/' + state + '/' + city + '.json'

	# Make the call to the api
	json_response = requests.get(target_url).json()

	return json_response

if __name__ == '__main__':
	wunderground_key = '887e3ed0a66ad9c9'
	city = 'Pasadena'
	state = 'CA'

	# Make the call to the api
	json_data = get_current_conditions_wunderground(wunderground_key, city, state)

	# Parse the response
	current_temp = parse_current_conditions_wunderground(json_data, 'temp')
	weather = parse_current_conditions_wunderground(json_data, 'weather')
	humidity = parse_current_conditions_wunderground(json_data, 'humidity')
	wind = parse_current_conditions_wunderground(json_data, 'wind')
	feels_like = parse_current_conditions_wunderground(json_data, 'feelslike')
	print(current_temp)
	print(weather)
	print(humidity)
	print(wind)
	print(feels_like)


