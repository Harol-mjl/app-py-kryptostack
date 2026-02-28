from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.users.v1 import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='users')
urlpatterns = [
    path('', include(router.urls)),
]