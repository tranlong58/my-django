from django.urls import path
from . import views

app_name = "login_page"
urlpatterns = [
    path('login/', views.login, name='login'),
    path('authen/', views.authen, name='authen'),
]