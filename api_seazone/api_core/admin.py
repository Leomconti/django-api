from anuncios.models import Anuncio
from django.contrib import admin
from imoveis.models import Imovel
from reservas.models import Reserva

admin.site.register(Imovel)
admin.site.register(Anuncio)
admin.site.register(Reserva)