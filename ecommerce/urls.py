from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.home.urls')),
    path('perfil/', include('apps.accounts.urls')),
    path('statistics/', include('apps.accounts.urls')),
    path('produtos/', include('apps.products.urls')),
    path('carrinho/', include('apps.cart.urls')),
    path('orders/', include('apps.orders.urls')),
    path('suporte/', include('apps.support.urls')),
]
