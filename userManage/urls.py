from .views import register,login, UsersViews
from django.urls import path, include
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('usuarios', UsersViews, basename='usuarios')
urlpatterns = [
path('registro/', register, name='registro'),
path('login/', login, name='login'),
path('',include(router.urls))
]