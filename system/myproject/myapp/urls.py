from django.urls import path
from . import views

urlpatterns = [
    path('', views.punch_page, name='punch_page'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('departments/', views.departments, name='departments'),
    path('add_employee/', views.add_employee, name='add_employee'),
    
]
