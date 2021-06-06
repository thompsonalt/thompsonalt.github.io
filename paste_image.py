import sys
from datetime import date
import pyperclip
from PIL import ImageGrab


im = ImageGrab.grabclipboard()

today = date.today()
cur_date = today.strftime("%y-%m-%d")

description = sys.argv[1]
im_location = 'assets/images/{}-{}.png'.format(cur_date, description)
im.save(im_location, 'PNG')

markdown = '![{}](/{})'.format(description, im_location)
pyperclip.copy(markdown)
