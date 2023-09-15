from django.core.management import call_command
from django.urls import reverse
from reservas.models import Reserva
from rest_framework import status
from rest_framework.test import APITestCase


class ReservaAPITests(APITestCase):    
    def setUp(self):
        call_command('loaddata', 'fixtures/imoveis_fixture.json')
        call_command('loaddata', 'fixtures/anuncios_fixture.json')
        call_command('loaddata', 'fixtures/reservas_fixture.json')
        self.reserva = Reserva.objects.first()
        self.url_get = reverse('reserva-detail', args=[self.reserva.pk])
        self.url_get_list = reverse('reserva-list')
        self.url_delete = reverse('reserva-delete', args=[self.reserva.pk])

    def test_create_reserva(self):
        url_create = reverse('reserva-create')
        data = {
            "anuncio": 1,
            "data_checkin": "2023-09-20",
            "data_checkout": "2023-09-25",
            "preco_total": 500.0,
            "numero_hospedes": 4
        }
        response = self.client.post(url_create, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_get_reserva(self):
        response = self.client.get(self.url_get)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data_criacao'], self.reserva.data_criacao.isoformat().replace('+00:00', 'Z'))

    def test_get_list(self):
        response = self.client.get(self.url_get_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Reserva.objects.count())

    def test_delete_reserva(self):
        response = self.client.delete(self.url_delete)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Reserva.objects.filter(pk=self.reserva.pk).exists())

    # Invalid ones, not found etc
    
    def test_get_reserva_not_found(self):
        url = reverse('reserva-detail', args=[99])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_reserva_not_found(self):
        url = reverse('reserva-delete', args=[99])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_reserva_invalid_anuncio(self):
        url_create = reverse('reserva-create')
        data = {
            "anuncio": 9999,
            "data_checkin": "2023-09-20",
            "data_checkout": "2023-09-25",
            "preco_total": 500.0,
            "numero_hospedes": 4
        }
        response = self.client.post(url_create, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_reserva_invalid_dates(self):
        url_create = reverse('reserva-create')
        data = {
            "anuncio": 1,
            "data_checkin": "2023-09-25",
            "data_checkout": "2023-09-20",
            "preco_total": 500.0,
            "numero_hospedes": 4
        }
        response = self.client.post(url_create, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)