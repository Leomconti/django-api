from django.urls import path
from imoveis import views

urlpatterns = [
    path('', views.get_list, name='imovel-list'),
    path('<int:pk>/', views.get, name='imovel-detail'),
    path('<int:pk>/delete/', views.delete, name='imovel-delete'),
    path('<int:pk>/patch/', views.patch, name='imovel-patch'),
]