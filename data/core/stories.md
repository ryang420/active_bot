## order pizza story
* greet
    - utter_greet
* order_pizza
    - utter_get_pizza_size
* order_pizza
    - utter_get_pizza_toppings
* order_pizza
    - action_order_pizza
    
## weather story
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "italy"}
    - slot{"location": "italy"}
    - action_weather
    - slot{"location": "italy"}
* thank
    - utter_thank

## Generated Story 5102548860608436662
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "italy"}
    - slot{"location": "italy"}
    - action_weather
    - slot{"location": "italy"}
* goodbye
    - utter_goodbye

## Generated Story -2463950199655988400
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "chengdu"}
    - slot{"location": "chengdu"}
    - action_weather
    - slot{"location": "chengdu"}
* goodbye
    - utter_goodbye

## Generated Story -3260268258962465565
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "china"}
    - slot{"location": "china"}
    - action_weather
* goodbye
    - utter_goodbye

## Generated Story 5026774370259720983
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "london"}
    - slot{"location": "london"}
    - action_weather
    - slot{"location": "london"}
* goodbye
    - utter_goodbye

## Generated Story -5052886794164103452
* greet
    - utter_greet
* inform{"location": "vilnius"}
    - slot{"location": "vilnius"}
    - action_weather
    - slot{"location": "vilnius"}
* goodbye
    - utter_goodbye


## Generated Story 944502499648864895
* greet
    - utter_greet
* order_pizza
    - utter_get_pizza_size
* order_pizza{"size": "large"}
    - slot{"size": "large"}
    - utter_get_pizza_toppings
* order_pizza{"toppings": "olives"}
    - slot{"toppings": "olives"}
    - action_order_pizza
    - slot{"size": "large"}
    - slot{"toppings": "olives"}
* goodbye
    - utter_goodbye

## Generated Story -952726643222063042
* thank
    - utter_thank

## Generated Story 5411064511977660461
* greet
    - utter_greet
* inform{"location": "italy"}
    - slot{"location": "italy"}
    - action_weather
    - slot{"location": "italy"}
* thank
    - utter_thank

