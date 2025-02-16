from django.shortcuts import render
from django.utils.timezone import now
from .models import DailyAccess
from .models import Users


def index(request):
    if request.user.is_authenticated:
        return render(request, 'accounts/index.html')
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'GET':
        return render(request, 'accounts/register.html')
    elif request.method == 'POST':
        return render(request, 'accounts/login.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html')
    elif request.method == 'POST':
        return render(request, 'accounts/index.html')

def statistics(request):
    today = now().date()
    total_acessos = DailyAccess.objects.filter(data=today).count()

    return render(request, 'accounts/statistics.html', {'total_acessos': total_acessos})
