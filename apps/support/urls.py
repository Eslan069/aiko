from django.urls import path
from . views import index

app_name = 'support'
urlpatterns = [
    path('', index, name='support'),
]