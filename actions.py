#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from utils.get_days import get_days


class ActionWeather(Action):
    def name(self):
        return 'action_weather'

    def run(self, dispatcher, tracker, domain):
        from apixu.client import ApixuClient
        api_key = '1425533582cd4b6db2c20015192801'
        client = ApixuClient(api_key)
        loc = tracker.get_slot('GPE')
        dt = tracker.get_slot('time')
        days = get_days(dt)

        weather_result = client.forecast(q=loc, days=days+1)
        condition = weather_result['forecast']['forecastday'][days]['day']['condition']['text']
        temperature_c = weather_result['forecast']['forecastday'][days]['day']['avgtemp_c']
        humidity = weather_result['forecast']['forecastday'][days]['day']['avghumidity']
        wind_mph = weather_result['forecast']['forecastday'][days]['day']['maxwind_mph']

        city = weather_result['location']['name']

        if days == 1:
            weather_time = 'tomorrow'
        elif days > 1:
            weather_time = dt[:10]
        else:
            weather_time = 'today'

        response = "The weather in {} is {} on {}. " \
                   "The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.".format(
            city, condition, weather_time, temperature_c, humidity, wind_mph)

        dispatcher.utter_message(response)
        return [SlotSet('GPE', loc)]
