from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('website/', views.home, name="home"), 
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
]