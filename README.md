### Summon Leviathan-Lemonade!

![Leviathan FFVII](https://github.com/Gusbenz/Leviathan-Lemonade/blob/master/FFVII_Leviathan.png)

> In such condition there is no place for industry, because the fruit thereof is uncertain, and consequently no culture of the earth, no navigation nor the use of commodities that may be imported by sea, no commodious building, no instruments of moving and removing such things as require much force, no knowledge of the face of the earth, no account of time, no arts, no letters, no society, and which is worst of all, continual fear and danger of violent death, and the life of man, solitary, poor, nasty, brutish, and short.

— *Thomas Hobbes*

> Middle fingers up /
Put them hands high /
Wave it in his face /
Tell 'em boy bye /
Tell 'em boy bye /
Boy bye /
Middle fingers up /
I ain't thinking 'bout you

— *Beyoncé*

### Python Scripts

1. New York Times Top World Stories LCD scroll
  * Does what it says above

```python
# Gives us what we need
import os
import I2C_LCD_driver
import requests
import json
from time import sleep
```

```python
# Assign some shiiiit
mylcd = I2C_LCD_driver.lcd()

# for scolling text on LCD
str_pad = " " * 16

# NYTimes API key
apiKey = os.environ['NY_TIMES_API_KEY']
```

```python
# Does it!
while True:
    r = requests.get(
        'https://api.nytimes.com/svc/topstories/v1/world.json?api-key=' + apiKey)
    data = r.json()
    jsonObj = data['results']
    for item in jsonObj:
        x = 1
        for i in range(0, len(item['title'])):
            lcd_text = item['title'][i:(i + 16)] + '.' + ' Story below.'
            mylcd.lcd_display_string(lcd_text, 1)
            sleep(0.2)
            x += 1
        if x > 1:
            for i in range(0, len(item['abstract'])):
                lcd_text2 = item['abstract'][i:(i + 16)] + '.'
                mylcd.lcd_display_string(lcd_text2, 2)
                sleep(0.3)
                x = 1
```
