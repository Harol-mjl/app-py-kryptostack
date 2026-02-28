from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=True)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.users.v1.urls')),
]
