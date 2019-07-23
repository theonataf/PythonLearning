from django.shortcuts import render
from menu_app.models import MenuItem
# Create your views here.


def show_menu(request):
    menu_items = MenuItem.objects.all()
    print(menu_items)
    return render(request, 'menu.html', context={'items': menu_items})
