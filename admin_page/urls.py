from django.urls import path
from .views import admin_views, logout_views

app_name = "admin_page"
urlpatterns = [
    path('logout/', logout_views.logout, name='admin-logout'),
    
    path('admins/', admin_views.index, name='admin-index'),
    path('admins/create/', admin_views.create, name='admin-create'),
    path('admins/update/', admin_views.update, name='admin-update'),
    path('admins/delete/', admin_views.delete, name='admin-delete'),
]