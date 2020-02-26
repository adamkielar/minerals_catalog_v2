from operator import attrgetter

from django.urls import reverse, resolve
from django.test import TestCase, Client

from .models import Mineral
from .views import mineral_list, mineral_detail, mineral_letter, mineral_search


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
            name='Curite',
            category='Oxide',
            group='Oxides'
        )

    def test_mineral_list_view(self):
        resp = self.client.get(reverse('minerals:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertIn(self.mineral2, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'layout.html')
        self.assertContains(resp, self.mineral.name)
        self.assertEqual(True, self.mineral.name.startswith('A'))

    def test_mineral_list_random_link_view(self):
        found = resolve('/1/')
        self.assertEqual(found.func, mineral_detail)

    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('minerals:detail',
                                       kwargs={'pk': self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, self.mineral.category)

    def test_mineral_letter_link_view(self):
        resp = self.client.get(reverse('minerals:letter',
                                       kwargs={'pk': 'A'}))
        found = resolve('/search/A/')
        self.assertEqual(found.func, mineral_letter)
        self.assertEqual(len(resp.context['minerals']), 1)

        resp = self.client.get(reverse('minerals:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, self.mineral.name)

    def test_mineral_search_view(self):
        resp = self.client.get(reverse('minerals:search'),
                               {
                                   'q': self.mineral2
                               })
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, self.mineral2.name)

    def test_filter_by_group(self):
        self.assertQuerysetEqual(
            (
                Mineral.objects.filter(group__startswith='Oxides')
            ), [
                'Oxides',
            ],
            attrgetter('group')
        )
