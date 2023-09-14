from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('imoveis/', include('imoveis.urls')),
    path('anuncios/', include('anuncios.urls')),
    path('reservas/', include('reservas.urls')),
]
