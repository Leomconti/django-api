from anuncios import views
from django.urls import path

urlpatterns = [
    path('', views.get_list, name='anuncio-list'),
    path('<int:pk>/', views.get, name='anuncio-detail'),
    path('<int:pk>/delete/', views.delete, name='anuncio-delete'),
]