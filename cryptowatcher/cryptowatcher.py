import os
import time
import requests

from datetime import datetime
from lib.waveshare_epd import epd2in7
from PIL import Image, ImageDraw, ImageFont

pic_dir = 'pic'
hosts = ['https://www.coindesk.com/price/dogecoin', 'https://www.cnbc.com/quotes/TSLA']

price_doge = 0.0
price_tesla = 0.0
images = []
fonts = []

lcd = None
buff = None
pencil = None

def main():
    global fonts, images, lcd, buff, pencil

    print("Initializing...")

    try:
        lcd = epd2in7.EPD()
        lcd.init()

        # Load res
        fonts.append(ImageFont.truetype(os.path.join(pic_dir, 'Square.ttf'), 32))
        fonts.append(ImageFont.truetype(os.path.join(pic_dir, 'Square.ttf'), 13))
        images.append(Image.open(os.path.join(pic_dir, 'doge.png')))
        images.append(Image.open(os.path.join(pic_dir, 'tesla.png')))

        time.sleep(5)
        while True:
            update_prices()
            clean()
            update()
            time.sleep(1800)
    except IOError as e:
        print("Error:", e)

def clean():
    global lcd, buff, pencil

    print("Cleaning...")
    # lcd.Clear(0x00)
    buff = Image.new(mode='1', size=(lcd.height, lcd.width), color=255)
    pencil = ImageDraw.Draw(buff)
    # time.sleep(3)

def update():
    global price_doge, price_tesla, fonts, pencil, buff, lcd, images

    pencil.text((100,25), '$ ' + str(price_doge), font=fonts[0], fill=0, align='center')
    buff.paste(images[0], (20, 10))

    pencil.text((100,115), '$ ' + str(price_tesla), font=fonts[0], fill=0, align='center')
    buff.paste(images[1], (20, 100))

    now = datetime.now()
    time = now.strftime("%H:%M ")
    pencil.text((225,160), time, font=fonts[1], fill=0, align='center')

    lcd.display(lcd.getbuffer(buff))

def update_prices():
    global price_doge, price_tesla, hosts

    print("Downloading prices...")
    try:
        resp = requests.get(hosts[0])
        resp.raise_for_status()
        data = resp.text
        index = data.find('<div class="price-large"><span class="symbol">$</span>')
        price_doge = float(data[index+54:data.find('</div>', index+54)][:-1])

        
        resp = requests.get(hosts[1])
        resp.raise_for_status()
        data = resp.text
        index = data.find('<span class="QuoteStrip-lastPrice">')
        price_tesla = float(data[index+35:data.find('</span>', index+35)])
    except Exception as e:
        print("Cannot reach server:", e)


if __name__ == '__main__':
    main()
