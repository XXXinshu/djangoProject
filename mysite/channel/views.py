from django.shortcuts import render, HttpResponseRedirect

from .models import User
from .forms import User_form

def userValid(fun):
    def inner(request, *args, **kwargs):
        user_id = request.COOKIES.get("user_id")
        if user_id:
            return fun(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/login/')
    return inner

@userValid

def index(request):
    return render(request, 'index/index_test.html')


def register(request):
    if request.method == 'POST' and request.POST:
        data = request.POST
        user_id = data.get('user_id')
        password = data.get('password')
        User.objects.create(
            user_id=user_id,
            password=password,
        )
        return HttpResponseRedirect('/login/')

    form = User_form()

    return render(request, 'register.html', context={'register_form': form})


def login(request):
    if request.method == 'POST' and request.POST:
        user_id = request.POST.get("user_id")
        password = request.POST.get("password")
        e = User.objects.filter(user_id=user_id).first()
        if e:
            db_password = e.password
            if password == db_password:
                response = HttpResponseRedirect('/index/')
                response.set_cookie("user_id", e.user_id)
                return response

    form = User_form()

    return render(request, "login.html", context={'login_form': form})

def logout(request):
    response = HttpResponseRedirect('/login/')
    response.delete_cookie("user_id")
    return response





