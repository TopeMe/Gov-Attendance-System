from django.urls import path
from . import views

urlpatterns = [
    path('', views.punch_page, name='punch_page'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    
]
