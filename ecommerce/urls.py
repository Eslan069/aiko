from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.accounts.urls')),
 #   path('products/', include('products.urls')),
 #   path('cart/', include('cart.urls')),
 #   path('orders/', include('orders.urls')),
 #   path('support/', include('support.urls')),
]
