from django.urls import include, path

urlpatterns = [
    path('imoveis/', include('imoveis.urls')),
    path('anuncios/', include('anuncios.urls')),
    path('reservas/', include('reservas.urls')),
]
