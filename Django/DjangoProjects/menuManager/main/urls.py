from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('hello/', views.hello, name="hello"),

    # path('login/', views.log_in, name='log_in'),
]
