from django.urls import reverse, resolve
from django.test import TestCase, Client

from .models import Mineral
from .views import mineral_detail

client = Client()


class MineralModelTest(TestCase):
    def setUp(self):
        Mineral.objects.create(name='Abelsonite')

    def test_mineral_creation(self):
        mineral = Mineral.objects.get(name='Abelsonite')
        self.assertTrue(mineral)


class MineralViewsTests(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
            name='Abelsonite',
            category='Organic'
        )
        self.mineral2 = Mineral.objects.create(
            name='Abernathyite',
            category='Arsenate'
        )

    def test_mineral_list_view(self):
        resp = self.client.get(reverse('minerals:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertIn(self.mineral2, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'layout.html')
        self.assertContains(resp, self.mineral.name)

    def test_mineral_list_random_link_view(self):
        found = resolve('/1/')
        self.assertEqual(found.func, mineral_detail)

    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('minerals:detail',
                                       kwargs={'pk': self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, self.mineral.category)
