#!/usr/bin/python

import os
import I2C_LCD_driver
import requests
import json
from time import sleep
import datetime

mylcd = I2C_LCD_driver.lcd()

#### Date / Time ####
currentDate = datetime.datetime.now()
hour = currentDate.hour
minute = currentDate.minute
####

#### NYTimes API key ####
apiKey = os.environ['NY_TIMES_API_KEY']
####

while True:
    if hour % 1 == 0 and minute != 00:
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
                sleep(0.4)
                mylcd.lcd_clear()
                x += 1
            if x > 1:
                for i in range(0, len(item['abstract'])):
                    lcd_text2 = item['abstract'][i:(i + 16)] + '.'
                    mylcd.lcd_display_string(lcd_text2, 2)
                    sleep(0.4)
                    mylcd.lcd_clear()
                    x = 1
    else:
        mylcd.lcd_display_string('Not Top Hour')
