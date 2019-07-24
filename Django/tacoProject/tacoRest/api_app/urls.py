from django.urls import path
from . import views

urlpatterns = [
    path('menuitem', views.menu_item, name='menu_item'),
    path('menuitem/<int:item_id>', views.delete_item, name="delete_item")
]
