# -*- coding: utf-8 -*-
from typing import Dict, Text, Any, List, Union
import time
from datetime import datetime

from apixu.client import ApixuException
from rasa_core_sdk import ActionExecutionRejection, Action
from rasa_core_sdk import Tracker
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT

from bot.TelegramBot import TelegramBot


class RestaurantForm(FormAction):
    """Example of a custom form action"""

    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""

        return "restaurant_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["cuisine", "num_people", "outdoor_seating",
                "preferences", "feedback"]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {"cuisine": self.from_entity(entity="cuisine",
                                            not_intent="chitchat"),
                "num_people": [self.from_entity(entity="num_people",
                                                intent=["inform",
                                                        "request_restaurant"]),
                               self.from_entity(entity="number")],
                "outdoor_seating": [self.from_entity(entity="seating"),
                                    self.from_intent(intent='affirm',
                                                     value=True),
                                    self.from_intent(intent='deny',
                                                     value=False)],
                "preferences": [self.from_intent(intent='deny',
                                                 value="no additional "
                                                       "preferences"),
                                self.from_text(not_intent="affirm")],
                "feedback": [self.from_entity(entity="feedback"),
                             self.from_text()]}

    @staticmethod
    def cuisine_db():
        # type: () -> List[Text]
        """Database of supported cuisines"""
        return ["caribbean",
                "chinese",
                "french",
                "greek",
                "indian",
                "italian",
                "mexican"]

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""
        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate(self,
                 dispatcher: CollectingDispatcher,
                 tracker: Tracker,
                 domain: Dict[Text, Any]) -> List[Dict]:
        """Validate extracted requested slot
            else reject the execution of the form action
        """
        # extract other slots that were not requested
        # but set by corresponding entity
        slot_values = self.extract_other_slots(dispatcher, tracker, domain)

        # extract requested slot
        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher,
                                                           tracker, domain))
            if not slot_values:
                # reject form action execution
                # if some slot was requested but nothing was extracted
                # it will allow other policies to predict another action
                raise ActionExecutionRejection(self.name(),
                                               "Failed to validate slot {0} "
                                               "with action {1}"
                                               "".format(slot_to_fill,
                                                         self.name()))

        # we'll check when validation failed in order
        # to add appropriate utterances
        for slot, value in slot_values.items():
            if slot == 'cuisine':
                if value.lower() not in self.cuisine_db():
                    dispatcher.utter_template('utter_wrong_cuisine', tracker)
                    # validation failed, set slot to None
                    slot_values[slot] = None

            elif slot == 'num_people':
                if not self.is_int(value) or int(value) <= 0:
                    dispatcher.utter_template('utter_wrong_num_people',
                                              tracker)
                    # validation failed, set slot to None
                    slot_values[slot] = None

            elif slot == 'outdoor_seating':
                if isinstance(value, str):
                    if 'out' in value:
                        # convert "out..." to True
                        slot_values[slot] = True
                    elif 'in' in value:
                        # convert "in..." to False
                        slot_values[slot] = False
                    else:
                        dispatcher.utter_template('utter_wrong_outdoor_seating',
                                                  tracker)
                        # validation failed, set slot to None
                        slot_values[slot] = None

        # validation succeed, set the slots values to the extracted values
        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_template('utter_submit', tracker)
        return []


class WeatherAction(Action):
    def name(self):
        return 'action_weather'

    def run(self, dispatcher, tracker, domain):
        from apixu.client import ApixuClient
        api_key = '1425533582cd4b6db2c20015192801'
        client = ApixuClient(api_key)

        loc = tracker.get_slot('location')

        forecast_date = tracker.get_slot('time')
        date_format = "%Y-%m-%d"
        today = time.strftime(date_format, time.localtime())
        if forecast_date is not None:
            forecast_date = forecast_date[:10]
        else:
            forecast_date = today

        delta = datetime.strptime(forecast_date, date_format) - datetime.strptime(today, date_format)

        forecast_weather = {}
        try:
            forecast_weather = client.forecast(q=loc, days=delta.days + 1)
        except ApixuException as e:
            print(e.message)
            dispatcher.utter_message('No matching location found. Please try again')

        forecast = [weather for weather in forecast_weather['forecast']['forecastday'] if
                    forecast_date in weather.values()]

        city = forecast_weather['location']['name']
        condition = forecast[0]['day']['condition']['text']
        temperature_c = forecast[0]['day']['avgtemp_c']

        response = f'The weather in {city} is {condition}, the temperature is {temperature_c}.'
        dispatcher.utter_message(response)
        return [SlotSet('location', loc)]


class RegistrationReportAction(Action):
    def name(self):
        return 'action_registration_report'

    def run(self,
            dispatcher,  # type: CollectingDispatcher
            tracker,  # type: Tracker
            domain  # type:  Dict[Text, Any]
            ):

        telegram_bot = TelegramBot('708856373:AAFcSklRew9msW8PUMWCB-d5gY7zz_GvTTw')
        # telegram_bot.send_image_url('615775632', 'https://i.ibb.co/1Zhqg7V/cat.jpg')
        with open('report.csv', 'rb') as f:
            telegram_bot.send_file('615775632', f)
        return []
