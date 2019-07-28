import json
from django.shortcuts import render
from django.http import JsonResponse
from api_app.models import MenuItem, Comment
# Create your views here.


def menu_item(request):
    if request.method == 'GET':
        all_items = MenuItem.objects.all()
        items = []

        for item in all_items:
            items.append({
                'id': item.id,
                'name': item.name,
                'lang': item.lang,
                'price': item.price,
                'page_title': item.page_title,
                'page_number': item.page_number,
                'page_position': item.page_position,
                'currency': item.currency
            })
        return JsonResponse({'code': 200, 'menuitems': items})

    elif request.method == 'POST':
        if request.headers['Authorization'] == 'pizdetz':
            request_body = json.loads(request.body.decode(encoding='UTF-8'))
            name = request_body['name']
            lang = request_body['lang']
            page_number = request_body['pagenumber']
            page_position = request_body['pageposition']
            price = request_body['price']
            currency = request_body['currency']
            page_title = request_body['pagetitle']

            MenuItem.objects.get_or_create(name=name, lang=lang, page_number=page_number,
                                           page_title=page_title, currency=currency, page_position=page_position, price=price)
            return JsonResponse({'code': 200, 'message': 'object_created'})


def delete_item(request, item_id):
    if request.method == 'DELETE':
        if request.headers['Authorization'] == 'pizdetz':
            item_object = MenuItem.objects.get(id=item_id)
            item_object.delete()
            return JsonResponse({
                "code": 200,
                "message": "item_deleted",
                "item": item_object.name
            })
