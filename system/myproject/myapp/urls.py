from django.urls import path
from . import views

urlpatterns = [
    path('', views.punch_page, name='punch_page'),
    path('admin_dashboard/', views.admin_dashboard_view, name='admin_dashboard'),
    path('login/', views.login_view, name='login'),  # Keep this as the login path
    path('departments/', views.departments, name='departments'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('logout/', views.logout_view, name='logout'),
]
