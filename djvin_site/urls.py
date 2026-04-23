"""
URL configuration for djvin_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import home, booking, music, payment, notifications, mark_notification_read, dashboard, export_bookings_csv, ping
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('booking/', booking, name='booking'),
    path('music/', music, name='music'),
    path('payment/', payment, name='payment'),
    path('ping/', ping),
    path('api/notifications/', notifications, name='notifications'),
    path('api/notifications/mark-read/', mark_notification_read, name='mark_notification_read'),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/export/', export_bookings_csv, name='export_bookings_csv'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
