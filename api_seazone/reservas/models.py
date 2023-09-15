import random
from datetime import datetime

from anuncios.models import Anuncio
from django.db import models
from rest_framework import serializers


def generate_reservation_code():
    """ as we are doing a code for a reservation, let's use the date it was created at, a random number just in case"""
    # Current date in YYMMDD format
    date_str = datetime.now().strftime("%y%m%d")

    return int(date_str + str(random.randint(100000, 999999)))

class Reserva(models.Model):
    codigo = models.PositiveIntegerField(primary_key=True, default=generate_reservation_code(), unique=True, editable=False)  # create a random unique id for each reservation
    anuncio = models.ForeignKey(Anuncio, on_delete=models.DO_NOTHING)  # one to many relationship
    data_checkin = models.DateField()
    data_checkout = models.DateField()
    preco_total = models.DecimalField(max_digits=10, decimal_places=2)
    comentario = models.TextField(blank=True, null=True)
    numero_hospedes = models.PositiveIntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True, null=True)



class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'