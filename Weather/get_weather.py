#!/usr/bin/env python3

import sys
import os
import re
import requests

def get_wunderground_key(key_path):
	# Import the public key
        key_fh = open(key_path, 'r')
        key_data = key_fh.readlines()
        key_fh.close()
        for line in key_data:
                if 'wunderground' in line:
                        api_key = re.split('=', line)[-1].strip()

	return api_key

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

def parse_forecast_wunderground(json_data, value):
	# Initialize variables
	return_value = None

	# Parse the data as needed
	if "high" in value: return_value = json_data["high"]["fahrenheit"]
	elif "low" in value: return_value = json_data["low"]["fahrenheit"]
	elif "humidity" in value: return_value = json_data["avehumidity"]
	elif "conditions" in value: return_value = json_data["Conditions"]

	return return_value

def get_forecast_wunderground(key_path, city, state):
	# Initialize the variables
	json_response = None

	# Import the API key
	api_key = get_wunderground_key(key_path)

	# Create the target url
	target_url = 'http://api.wunderground.com/api/' + api_key + '/forecast/q/' + state + '/' + city + '.json'

	# Make the call to the api
	json_response = requests.get(target_url).json()
	
	# Get the data for the current day
	current_day_json = json_response['forecast']['simpleforecast']['forecastday'][0]

	return current_day_json


def get_current_conditions_wunderground(key_path, city, state):
	# Initialize the variables
	json_response = None	

	# Import the API key
	api_key = get_wunderground_key(key_path)

	# Create the target url
	target_url = 'http://api.wunderground.com/api/' + api_key + '/conditions/q/' + state + '/' + city + '.json'

	# Make the call to the api
	json_response = requests.get(target_url).json()

	return json_response

if __name__ == '__main__':
	key_path = '/home/pi/APIKeys'
	city = 'Pasadena'
	state = 'CA'

	# Make the call to the api
	json_data = get_forecast_wunderground(key_path, city, state)

	# Parse the response
	high = parse_forecast_wunderground(json_data, 'high')
	low = parse_forecast_wunderground(json_data, 'low')
	print(high)
	print(low)


