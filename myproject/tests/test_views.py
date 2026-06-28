from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):

    def setUp(self):
        Menu.objects.create(
            name="Pizza",
            price=250,
            menu_item_description="Cheese Pizza"
        )

        Menu.objects.create(
            name="Burger",
            price=180,
            menu_item_description="Veg Burger"
        )

        self.client = APIClient()

    def test_getall(self):
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)

        response = self.client.get('/restaurant/menu-items/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)