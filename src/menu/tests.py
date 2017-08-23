from django.test import TestCase
from django.urls import reverse_lazy
from django.utils import timezone

from .models import (
    Menu,
    Dish,
)


class MenuListTest(TestCase):
    url = reverse_lazy('menu_list')

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)


class MenuListAPIViewTest(TestCase):
    url = reverse_lazy('api_menu_list')

    def setUp(self):
        self.menu = Menu.objects.create(name='Name', description='Description')
        self.dish = Dish.objects.create(
            menu=self.menu, name='Name', description='Description',
            price=10, preparation_time=timezone.timedelta(seconds=1260)
        )

    def test_get(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(
            dict(response.data['results'][0]),
            {'id': self.menu.id, 'name': self.menu.name, 'dish_number': 1, 'description': self.menu.description}
        )

    def test_get_return_only_menu_that_contains_dishes(self):
        Menu.objects.create(name='Name2', description='Description')

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)


class DishListAPITest(TestCase):
    url = reverse_lazy('api_dish_list')

    def setUp(self):
        self.menu = Menu.objects.create(name='Name', description='Description')
        self.price = '10.00'
        self.dish = Dish.objects.create(
            menu=self.menu, name='Name', description='Description',
            price=self.price, preparation_time=timezone.timedelta(seconds=1260)
        )

    def test_get(self):
        response = self.client.get(self.url, {'id': self.menu.id})

        self.assertEqual(response.status_code, 200)
        self.assertListEqual(
            list(response.data[0].keys()),
            ['name', 'description', 'price', 'preparation_time', 'is_vegetarian']
        )

    def test_get_return_only_selected_menu_dishes(self):
        menu = Menu.objects.create(name='Name2', description='Description')
        Dish.objects.create(
            menu=menu, name='Name', description='Description',
            price=self.price, preparation_time=timezone.timedelta(seconds=1260)
        )

        response = self.client.get(self.url, {'id': self.menu.id})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
