from django.test import SimpleTestCase
from django.urls import reverse


class AboutPageTests(SimpleTestCase):
    def test_existe_ruta(self):
        response = self.client.get("/pages/about")
        self.assertEqual(response.status_code, 200)
        
    def test_nombre_ruta_about(self):
        response = self.client.get(reverse("pages:about"))
        self.assertEqual(response.status_code, 200)
        
    def test_plantilla_contiene_html(self):
        response = self.client.get(reverse("pages:about"))
        self.assertContains(response, "Aplicacion Elaborada para el Curso de Django para Profecionales")
        
    def test_plantilla_no_contiene_html(self):
        response = self.client.get(reverse("pages:about"))
        self.assertNotContains(response, "KENTO")