import uuid

from django.db import models

from anuncios.models import Anuncio


class Reserva(models.Model):
    codigo = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)  # create a random unique id for each reservation
    anuncio = models.ForeignKey(Anuncio, on_delete=models.DO_NOTHING)  # one to many relationship
    data_checkin = models.DateField()
    data_checkout = models.DateField()
    preco_total = models.DecimalField(max_digits=10, decimal_places=2)
    comentario = models.TextField(blank=True, null=True)
    numero_hospedes = models.PositiveIntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    