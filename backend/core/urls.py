from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('events.urls')),
    path('api/payments/', include('payments.urls')),
]