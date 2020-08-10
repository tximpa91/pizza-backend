from django.test import TestCase, Client
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from pizza_app.serializers import Pizza, PizzaSerializer

# Create your tests here.
client = Client()


class GetAllPizzasTest(APITestCase):
    """ Test module for GET all puppies API """

    def setUp(self):
        pass

    def test_get_all_pizzas(self):
        # get API response
        pizzas = reverse('pizza')
        response = self.client.get(pizzas)
        # get data from db
        pizzas = Pizza.objects.all()
        serializer = PizzaSerializer(pizzas, many=True)
        self.assertEqual(response.data, {"status": status.HTTP_200_OK,
                                         "total": len(serializer.data), "data": serializer.data})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
