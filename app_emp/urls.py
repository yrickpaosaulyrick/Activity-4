from django.urls import path
from . import views
from .views import logout_view

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/', views.add_employee, name='add_employee'),
    path('edit/<int:id>/', views.edit_employee, name='edit_employee'),
    path('delete/<int:id>/', views.delete_employee, name='delete_employee'),
    path('logout/', logout_view, name='logout'),
]
