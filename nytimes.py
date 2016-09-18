#!/usr/bin/python

import os
import I2C_LCD_driver
import requests
import json
from time import sleep

mylcd = I2C_LCD_driver.lcd()

# NYTimes API key
apiKey = os.environ['NY_TIMES_API_KEY']

while True:
    mylcd.lcd_clear()
    r = requests.get(
        'https://api.nytimes.com/svc/topstories/v1/world.json?api-key=' + apiKey)
    data = r.json()
    jsonObj = data['results']
    for item in jsonObj:
        x = 1
        for i in range(0, len(item['title'])):
            lcd_text = item['title'][i:(i + 16)] + ':'
            mylcd.lcd_display_string(lcd_text, 1)
            sleep(0.2)
            mylcd.lcd_clear()
            x += 1
        if x > 1:
            for i in range(0, len(item['abstract'])):
                lcd_text2 = item['abstract'][i:(i + 16)] + '.'
                mylcd.lcd_display_string(lcd_text2, 2)
                sleep(0.3)
                mylcd.lcd_clear()
                x = 1
