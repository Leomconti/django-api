from django.urls import path
from imoveis import views

urlpatterns = [
    path('create/', views.create, name='imovel-create'),
    path('', views.get_list, name='imovel-list'),
    path('<int:pk>/', views.get, name='imovel-detail'),
    path('<int:pk>/delete/', views.delete, name='imovel-delete'),
    path('<int:pk>/patch/', views.patch, name='imovel-patch'),
]