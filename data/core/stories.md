## weather story
* greet
    - utter_greet
* weather_forecast
    - utter_ask_location
* weather_forecast{"location": "italy"}
    - slot{"location": "italy"}
    - action_weather
    - slot{"location": "italy"}
* thankyou
    - utter_thank

## Generated Story 844443453536116190
* greet
    - utter_greet
* weather_forecast
    - utter_ask_location
* weather_forecast{"location": "london"}
    - slot{"location": "london"}
    - action_weather
    - slot{"location": "london"}
* thankyou
    - utter_thank

## Generated Story 2314998157492792314
* greet
    - utter_greet
* weather_forecast{"location": "berlin"}
    - slot{"location": "berlin"}
    - action_weather
    - slot{"location": "berlin"}
* thankyou
    - utter_thank

## Generated Story -5651366554831124349
* greet
    - utter_greet
* weather_forecast{"location": "Dallas"}
    - slot{"location": "Dallas"}
    - action_weather
    - slot{"location": "Dallas"}

## Generated Story -8683364652006619164
* greet
    - utter_greet
* weather_forecast{"location": "Dallas"}
    - slot{"location": "Dallas"}
    - action_weather
    - slot{"location": "Dallas"}
* weather_forecast{"location": "Shanghai"}
    - slot{"location": "Shanghai"}
    - action_weather
    - slot{"location": "Shanghai"}
* thankyou
    - utter_thank

## Generated Story -8358912192954647627
* greet
    - utter_greet
* weather_forecast
    - utter_ask_location
* weather_forecast{"location": "Shanghai"}
    - slot{"location": "Shanghai"}
    - action_weather
    - slot{"location": "Shanghai"}
* thankyou
    - utter_thank

## Generated Story -5610980595821978015
* weather_forecast{"location": "shanghai"}
    - slot{"location": "shanghai"}
    - action_weather
    - slot{"location": "shanghai"}
* weather_forecast{"location": "wuhan"}
    - slot{"location": "wuhan"}
    - action_weather
    - slot{"location": "wuhan"}
* thankyou
    - utter_thank

## Generated Story -1433056051729551907
* weather_forecast{"location": "beijing"}
    - slot{"location": "beijing"}
    - action_weather
* weather_forecast{"location": "xian"}
    - slot{"location": "xian"}
    - action_weather
* thankyou
    - utter_thank


## happy path
* greet
    - utter_greet
* request_restaurant
    - restaurant_form
    - form{"name": "restaurant_form"}
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries

## unhappy path
* greet
    - utter_greet
* request_restaurant
    - restaurant_form
    - form{"name": "restaurant_form"}
* chitchat
    - utter_chitchat
    - restaurant_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries

## very unhappy path
* greet
    - utter_greet
* request_restaurant
    - restaurant_form
    - form{"name": "restaurant_form"}
* chitchat
    - utter_chitchat
    - restaurant_form
* chitchat
    - utter_chitchat
    - restaurant_form
* chitchat
    - utter_chitchat
    - restaurant_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries

## stop but continue path
* greet
    - utter_greet
* request_restaurant
    - restaurant_form
    - form{"name": "restaurant_form"}
* stop
    - utter_ask_continue
* affirm
    - restaurant_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries

## stop and really stop path
* greet
    - utter_greet
* request_restaurant
    - restaurant_form
    - form{"name": "restaurant_form"}
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}

## chitchat stop but continue path
* request_restaurant
    - restaurant_form
    - form{"name": "restaurant_form"}
* chitchat
    - utter_chitchat
    - restaurant_form
* stop
    - utter_ask_continue
* affirm
    - restaurant_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries

## stop but continue and chitchat path
* greet
    - utter_greet
* request_restaurant
    - restaurant_form
    - form{"name": "restaurant_form"}
* stop
    - utter_ask_continue
* affirm
    - restaurant_form
* chitchat
    - utter_chitchat
    - restaurant_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries

## chitchat stop but continue and chitchat path
* greet
    - utter_greet
* request_restaurant
    - restaurant_form
    - form{"name": "restaurant_form"}
* chitchat
    - utter_chitchat
    - restaurant_form
* stop
    - utter_ask_continue
* affirm
    - restaurant_form
* chitchat
    - utter_chitchat
    - restaurant_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries

## chitchat, stop and really stop path
* greet
    - utter_greet
* request_restaurant
    - restaurant_form
    - form{"name": "restaurant_form"}
* chitchat
    - utter_chitchat
    - restaurant_form
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}

## Generated Story 3490283781720101690 (example from interactive learning, "form: " will be excluded from training)
* greet
    - utter_greet
* request_restaurant
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "cuisine"}
* chitchat
    - utter_chitchat  <!-- restaurant_form was predicted by FormPolicy and rejected, other policy predicted utter_chitchat -->
    - restaurant_form
    - slot{"requested_slot": "cuisine"}
* form: inform{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - form: restaurant_form
    - slot{"cuisine": "mexican"}
    - slot{"requested_slot": "num_people"}
* form: inform{"number": "2"}
    - form: restaurant_form
    - slot{"num_people": "2"}
    - slot{"requested_slot": "outdoor_seating"}
* chitchat
    - utter_chitchat
    - restaurant_form
    - slot{"requested_slot": "outdoor_seating"}
* stop
    - utter_ask_continue
* affirm
    - restaurant_form  <!-- FormPolicy predicted FormValidation(False), other policy predicted restaurant_form -->
    - slot{"requested_slot": "outdoor_seating"}
* form: affirm
    - form: restaurant_form
    - slot{"outdoor_seating": true}
    - slot{"requested_slot": "preferences"}
* form: inform
    - form: restaurant_form
    - slot{"preferences": "/inform"}
    - slot{"requested_slot": "feedback"}
* form: inform{"feedback": "great"}
    - slot{"feedback": "great"}
    - form: restaurant_form
    - slot{"feedback": "great"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_slots_values
* thankyou
    - utter_noworries

## Generated Story -4729505263493939273
* greet
    - utter_greet
* weather_forecast
    - utter_ask_location
* weather_forecast{"location": "Tokyo"}
    - slot{"location": "Tokyo"}
    - action_weather
    - slot{"location": "Tokyo"}

## Generated Story 2650468281876918784
* greet
    - utter_greet
* weather_forecast
    - utter_ask_location
* weather_forecast{"location": "xian"}
    - slot{"location": "xian"}
    - action_weather
    - slot{"location": "xian"}
* thankyou
    - utter_thank

