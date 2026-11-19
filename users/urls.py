from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    # Django's built-in login and logout
    path('', include('django.contrib.auth.urls')),
    # Registration page
    path('register/', views.register, name='register'),
]