from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

from .forms import CustomUserCreationForm
from .views import RegistroUsuarioView


class CustomUserTest(TestCase):
    def test_crear_usuario(self):
        Usr = get_user_model()
        usr = Usr.objects.create_user(
            username = "kento",
            email = "kento@gmail.com",
            password = "123"
        )
        
        #Que esperamos
        self.assertEqual(usr.username,"kento")
        self.assertEqual(usr.email,"kento@gmail.com")
        self.assertTrue(usr.is_active)
        self.assertFalse(usr.is_staff)
        self.assertFalse(usr.is_superuser)
        
    def test_crear_superusuario(self):
        Usr = get_user_model()
        usr = Usr.objects.create_superuser(
            username = "kento",
            email = "kento@gmail.com",
            password = "123"
        )
        
        #Que esperamos
        self.assertEqual(usr.username,"kento")
        self.assertEqual(usr.email,"kento@gmail.com")
        self.assertTrue(usr.is_active)
        self.assertTrue(usr.is_staff)
        self.assertTrue(usr.is_superuser)
        
        
class RegistroUsuarioTest(TestCase):
    def setUp(self):
            url = reverse("usuarios:registro")
            self.response = self.client.get(url)
            
    def test_plantilla_registro(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "usuarios/registro.html")
        self.assertContains(self.response, "Registro")
        self.assertNotContains(self.response, "Bienvenido")
        
    def test_regisgro_form(self):
        form = self.response.context.get("form")
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, "csrfmiddlewaretoken")
        
    def test_registro_vista(self):
        view = resolve("/usuarios/registro/")
        self.assertEqual(view.func.__name__, RegistroUsuarioView.as_view().__name__)