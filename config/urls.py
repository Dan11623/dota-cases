from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('billing/', include('users_billing.urls')),
    path('inventory/', include('inventory.urls')),
    path('', include('cases.urls')),
]
