from django.urls import path
from . views import index
from . views import register
from . views import login
from .views import statistics

app_name = 'accounts'
urlpatterns = [
    path('', index, name='index'),
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('statistics', statistics, name='statistics'),
]
