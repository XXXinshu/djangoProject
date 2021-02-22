from django.contrib import admin
from django.urls import path
from channel.views import index, register, login, logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('register/', register),
    path('login/', login),
    path('logout/', logout)
]
