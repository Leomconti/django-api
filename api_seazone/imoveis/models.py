from django.db import models
from rest_framework import serializers


class Imovel(models.Model):
    codigo = models.PositiveIntegerField(primary_key=True, unique=True)
    limite_hospedes = models.PositiveIntegerField()  # more then 1000 is not necessary (I think?)
    quantidade_banheiros = models.PositiveIntegerField()
    aceita_animais_estimacao = models.BooleanField(default=False)
    valor_limpeza = models.DecimalField(max_digits=6, decimal_places=2)
    data_ativacao = models.DateField()
    data_criacao = models.DateTimeField(auto_now_add=True)  # added when the object is created
    data_atualizacao = models.DateTimeField(auto_now=True, null=True)  # add when the object is updated

class ImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imovel
        fields = '__all__'
        