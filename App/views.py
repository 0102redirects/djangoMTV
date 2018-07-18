import hashlib
import os
import uuid


from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import UserModel
from djangoMTV import settings


def index(request):
    return HttpResponse('index')


def uolade(request):
    if request.method == 'GET':
        return render(request, 'uoloade.html')
    elif request.method == 'POST':
        icon = request.FILES.get('icon')
        save_file_path = os.path.join(settings.BASE_DIR, 'static/uploade/' + str(uuid.uuid4()) + str(icon))

        with open(save_file_path, 'wb') as save_file:
            for part in icon.chunks():
                save_file.write(part)
                save_file.flush()
        return HttpResponse('上传成功')


def user_register(request):
    if request.method == 'GET':
        return render(request, 'user_register.html')
    elif request.method == 'POST':
        icon = request.FILES.get('icon')

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = UserModel()
        user.u_name = username
        password = genart_password(password)
        user.u_password = password
        user.u_icon = icon

        user.save()
        response = HttpResponse('注册成功')

        response.set_cookie('username', username)

        return response


def user_center(request):
    username = request.COOKIES.get("username")

    if not username:
        return render(request, 'user_center.html', context={"is_login": False})

    user = UserModel.objects.get(u_name=username)

    data = {
        "is_login": True,
        "username": user.u_name,
        "icon": "/static/uploade/" + user.u_icon.url
    }

    return render(request, 'user_center.html', context=data)

def genart_password(password):
    sha512 = hashlib.sha512()
    sha512.update(password.encode('utf8'))
    return sha512.hexdigest()