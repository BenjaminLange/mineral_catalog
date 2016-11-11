from django.shortcuts import reverse
from django.test import TestCase

from .models import Mineral


class MineralModelTests(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
            name="Abelsonite",
            image_filename="240px-Abelsonite_-_Green_River_Formation,_Uintah_County,_Utah,_USA.jpg",
            image_caption="Abelsonite from the Green River Formation, Uintah County, Utah, US",
            category="Organic",
            formula="C<sub>31</sub>H<sub>32</sub>N<sub>4</sub>Ni",
            strunz_classification="10.CA.20",
            crystal_system="Triclinic",
            unit_cell="a = 8.508 Å, b = 11.185 Åc=7.299 Å, α = 90.85°β = 114.1°, γ = 79.99°Z = 1",
            color="Pink-purple, dark greyish purple, pale purplish red, reddish brown",
            crystal_symmetry="Space group: P1 or P1Point group: 1 or 1",
            cleavage="Probable on {111}",
            mohs_scale_hardness="2–3",
            luster="Adamantine, sub-metallic",
            streak="Pink",
            diaphaneity="Semitransparent",
            optical_properties="Biaxial",
        )

    def test_mineral_creation(self):
        self.assertTrue(isinstance(self.mineral, Mineral))
        self.assertEqual(self.mineral.__str__(), self.mineral.name)


class ViewTests(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
            name="Abelsonite",
            image_filename="240px-Abelsonite_-_Green_River_Formation,_Uintah_County,_Utah,_USA.jpg",
            image_caption="Abelsonite from the Green River Formation, Uintah County, Utah, US",
            category="Organic",
            formula="C<sub>31</sub>H<sub>32</sub>N<sub>4</sub>Ni",
            strunz_classification="10.CA.20",
            crystal_system="Triclinic",
            unit_cell="a = 8.508 Å, b = 11.185 Åc=7.299 Å, α = 90.85°β = 114.1°, γ = 79.99°Z = 1",
            color="Pink-purple, dark greyish purple, pale purplish red, reddish brown",
            crystal_symmetry="Space group: P1 or P1Point group: 1 or 1",
            cleavage="Probable on {111}",
            mohs_scale_hardness="2–3",
            luster="Adamantine, sub-metallic",
            streak="Pink",
            diaphaneity="Semitransparent",
            optical_properties="Biaxial",
        )

    def test_mineral_index_view(self):
        resp = self.client.get(reverse('minerals:index'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/index.html')

    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('minerals:detail', kwargs={'pk': self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral, resp.context['mineral'])
        self.assertTemplateUsed(resp, 'minerals/detail.html')

    def test_mineral_random_view(self):
        resp = self.client.get(reverse('minerals:random'), follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals/detail.html')
