import django
import os
import json
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tacoRest.settings')
django.setup()

from api_app.models import MenuItem


with open('items.json', 'r') as f:
    items = json.load(f)
    menu_items = items['menuitems']

for item in menu_items:
    name = item['name']
    lang = item['lang']
    page_number = item['pagenumber']
    page_position = item['pageposition']
    price = item['price']
    currency = item['currency']
    page_title = item['pagetitle']

    MenuItem.objects.get_or_create(name=name, lang=lang, page_number=page_number, page_title=page_title, 
    currency=currency, page_position=page_position, price=price)
