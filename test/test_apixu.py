#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from apixu.client import ApixuClient

client = ApixuClient('1425533582cd4b6db2c20015192801')

forecast = client.forecast(q='Chengdu', days=3)

print(forecast['location']['name'])
print(forecast['forecast']['forecastday'])