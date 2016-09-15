#!/usr/bin/python

import os
import I2C_LCD_driver
import requests
import json
from time import sleep

mylcd = I2C_LCD_driver.lcd()

# for scolling text on LCD
str_pad = " " * 16

# NYTimes API key
apiKey = os.environ['NY_TIMES_API_KEY']

while True:
    r = requests.get(
        'https://api.nytimes.com/svc/topstories/v1/world.json?api-key=' + apiKey)
    data = r.json()
    jsonObj = data['results']
    for item in jsonObj:
        for i in range(0, len(item['abstract'])):
            lcd_text = item['abstract'][i:(i + 16)] + '.'
            mylcd.lcd_display_string(lcd_text, 1)
            mylcd.lcd_display_string('NYT Headlines', 2)
            sleep(0.3)
        sleep(1.0)
