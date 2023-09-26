from django.test import SimpleTestCase


class HomePageTests(SimpleTestCase):
    def setUp(self):
        self.response = self.client.get("")
    
    def test_url_home(self):
        self.assertEqual(self.response.status_code, 200)
        
    def test_html_home(self):
        self.assertTemplateUsed(self.response, "bases/home.html")
        self.assertContains(self.response, "Inicio")
        self.assertNotContains(self.response, "KENTO")