from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse

# Create your views here.


def index(request):
    hello = {'hebrew': 'shalom', 'french': 'bonjour', 'spanish': 'hola'}
    return render(request, 'index.html', context={'say_hello': hello})


def hello(request):
    users = User.objects.all()
    print('################')
    print(users)

    return render(request, 'hello.html', context={'users': users})


def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            result_data = {
                'code': 200,
                'username': username,
                'user_id': user.id,
            }
            return JsonResponse(result_data)
        else:
            result_data = {
                'code': 403,
                'message': 'user not found'
            }
            return JsonResponse(result_data)
    else:
        return JsonResponse({'code': 404, 'message': 'method not allowed'})
