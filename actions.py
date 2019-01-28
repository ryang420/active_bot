#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet


class ActionWeather(Action):
    def name(self):
        return 'action_weather'

    def run(self, dispatcher, tracker, domain):
        from apixu.client import ApixuClient
        api_key = '1425533582cd4b6db2c20015192801'
        client = ApixuClient(api_key)
        loc = tracker.get_slot('location')
        current = client.current(q=loc)

        country = current['location']['country']
        city = current['location']['name']
        condition = current['current']['condition']['text']
        temperature_c = current['current']['temp_c']
        humidity = current['current']['humidity']
        wind_mph = current['current']['wind_mph']

        response = """It is currently {} in {}, {} at the moment. 
                    The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(
            condition, city, country, temperature_c, humidity, wind_mph)

        dispatcher.utter_message(response)
        return [SlotSet('location', loc)]
