from django.test import TestCase
from django.urls import reverse

from .models import Mark, Modelo


class ModeloTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.modelo = Modelo.objects.create(
            mark = Mark.objects.create(decript = "Toyota"),
            descript = "Rush"
        )
        
    def test_lista(self):
        self.assertEqual(self.modelo.descript,"Rush")
        self.assertEqual(self.modelo.mark.decript,"Toyota")
        
    # def test_vista_modelo(self):
    #     response = self.client.get(reverse("control:modelo_list"))        
    #     self.assertEqual(response.status_code,200)        
    #     self.assertContains(response,"Rush")
    #     self.assertTemplateUsed(response,"ctrl_comb/modelo.html")
        
    # def test_vista_marcas(self):
    #     response = self.client.get(reverse("control:mark_list"))
    #     self.assertEqual(response.status_code,200)
    #     self.assertContains(response,"Toyota")
    #     self.assertTemplateUsed(response,"ctrl_comb/mark.html")
        
    def test_vista_modal(self):
        response = self.client.get(reverse("control:modelo_edit_modal",kwargs={'pk':self.modelo.id}))    #type: ignore
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Rush")
        self.assertTemplateUsed(response,"ctrl_comb/modelo_modal.html")