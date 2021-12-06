from django.test import TestCase, Client
from django.test.utils import setup_test_environment

from animals.models import Animal


class AnimalTestCase(TestCase):
    def setUp(self) -> None:
        Animal.objects.create(name="lion", sound="roar")
        Animal.objects.create(name="cat", sound="meow")
        # setup_test_environment()
        self.client = Client()

    def test_animals_can_speak(self):
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")

        self.assertEqual(lion.speak(), "The lion says roar")
        self.assertEqual(cat.speak(), "The cat says meow")
        self.assertIs(lion.name == 'lion', True)

    def test_template_renders(self):
        response = self.client.get('/animals')
        self.assertEqual(response.status_code, 404)
