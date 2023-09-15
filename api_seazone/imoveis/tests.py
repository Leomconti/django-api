from django.core.management import call_command
from django.urls import reverse
from imoveis.models import Imovel
from rest_framework import status
from rest_framework.test import APITestCase


class ImovelAPITests(APITestCase):    
    def setUp(self):
        call_command('loaddata', 'fixtures/imoveis_fixture.json')
        self.imovel = Imovel.objects.first()
        self.url_get = reverse('imovel-detail', args=[self.imovel.pk])
        self.url_get_list = reverse('imovel-list')
        self.url_delete = reverse('imovel-delete', args=[self.imovel.pk])
        self.url_patch = reverse('imovel-patch', args=[self.imovel.pk])


    def test_get_imovel(self):
        response = self.client.get(self.url_get)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data_criacao'], self.imovel.data_criacao.isoformat().replace('+00:00', 'Z'))  # the way timezones are handled is different

    def test_get_list(self):
        response = self.client.get(self.url_get_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Imovel.objects.count())

    def test_delete_imovel(self):
        response = self.client.delete(self.url_delete)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Imovel.objects.filter(pk=self.imovel.pk).exists())
        
    def test_patch_imovel(self):
        data = {'limite_hospedes': 20}
        response = self.client.patch(self.url_patch, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.imovel.refresh_from_db()
        self.assertEqual(self.imovel.limite_hospedes, 20)
        
    # invalid ones , not found etc

    def test_get_imovel_not_found(self):
        url = reverse('imovel-detail', args=[9999])  # Assuming 9999 is an ID that doesn't exist
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_delete_imovel_not_found(self):
        url = reverse('imovel-delete', args=[9999])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_patch_imovel_invalid_data(self):
        data = {'limite_hospedes': ''}  # Assuming name cannot be empty
        response = self.client.patch(self.url_patch, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_patch_imovel_not_found(self):
        url = reverse('imovel-patch', args=[9999])
        data = {'limite_hospedes': 21}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)