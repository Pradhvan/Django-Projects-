from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import bank
from .serializers import BankSerializer


class BaseViewTest(APITestCase):
    Client = APIClient()

    @staticmethod
    def create_bank(name="", bkid=""):
        if name != "" and bkid != "":
            bank.objects.create(name=name, bkid=bkid)

    def setup(self):
        self.create_bank("BOB", "1")
        self.create_bank("SBI", "2")
        self.create_bank("PNB", "3")


class GetAllBankTest(BaseViewTest):

    def test_get_all_banks(self):
        response = self.Client.get(
            reverse('all-banks')
        )
        expected = bank.objects.all()
        seralized = BankSerializer(many=True)
        self.assertEqual(response.data, seralized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
