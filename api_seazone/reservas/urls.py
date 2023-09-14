from django.urls import path
from reservas import views

urlpatterns = [
    path('', views.get_list, name='reserva-list'),
    path('<int:pk>/', views.get, name='reserva-detail'),
    path('<int:pk>/delete/', views.delete, name='reserva-delete'),
]