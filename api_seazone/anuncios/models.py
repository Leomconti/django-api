from django.db import models
from imoveis.models import Imovel
from rest_framework import serializers


class Anuncio(models.Model):
    imovel = models.ForeignKey(Imovel, on_delete=models.DO_NOTHING)  # no need to cascade, if anuncio is gone, the imovel is still there
    nome_plataforma = models.CharField(max_length=255)
    taxa_plataforma = models.DecimalField(max_digits=10, decimal_places=2)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    

class AnuncioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anuncio
        fields = '__all__'