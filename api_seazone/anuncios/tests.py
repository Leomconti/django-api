from anuncios.models import Anuncio
from django.core.management import call_command
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AnuncioAPITests(APITestCase):    
    def setUp(self):
        call_command('loaddata', 'fixtures/imoveis_fixture.json')
        call_command('loaddata', 'fixtures/anuncios_fixture.json')
        self.anuncio = Anuncio.objects.first()
        self.url_get = reverse('anuncio-detail', args=[self.anuncio.pk])
        self.url_get_list = reverse('anuncio-list')
        self.url_delete = reverse('anuncio-delete', args=[self.anuncio.pk])

    def test_get_anuncio(self):
        response = self.client.get(self.url_get)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Assuming Anuncio has a 'data_criacao' field similar to Reserva
        self.assertEqual(response.data['data_criacao'], self.anuncio.data_criacao.isoformat().replace('+00:00', 'Z'))

    def test_get_list(self):
        response = self.client.get(self.url_get_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Anuncio.objects.count())

    def test_delete_anuncio(self):
        response = self.client.delete(self.url_delete)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Anuncio.objects.filter(pk=self.anuncio.pk).exists())

    # Invalid ones, not found etc
    
    def test_get_anuncio_not_found(self):
        url = reverse('anuncio-detail', args=[9999])  # Assuming 9999 is an ID that doesn't exist
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_anuncio_not_found(self):
        url = reverse('anuncio-delete', args=[9999])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
