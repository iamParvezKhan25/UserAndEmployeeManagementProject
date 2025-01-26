from django.urls import path

from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path('', views.user_list, name='user_list'),
    path('employees/', views.employee_list, name='employee_list'),
    path('employee/<int:id>/', views.employee_detail, name='employee_detail'),
    path('user/<int:id>/', views.user_detail, name='user_detail'),
    path('user/add/', views.add_user, name='add_user'),
    path('employee/add/', views.add_employee, name='add_employee'),
    path('delete_employee/<int:id>/delete', views.delete_employee, name='delete_employee'),
    path('delete_user/<int:id>/', views.delete_user, name='delete_user'),


]