from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from .models import  Dispositivo


class LoginAdminViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_login_admin_view_get(self):
        response = self.client.get(reverse('login_admin'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'usAdmin/index.html')

    def test_login_admin_view_post_success(self):
        response = self.client.post(reverse('login_admin'), {'idNumber': 'testuser', 'password': '12345'})
        self.assertEqual(response.status_code, 200)  # Ajusta el código de estado según tu redirección
        self.assertTemplateUsed(response, 'usAdmin/index.html')

    def test_login_admin_view_post_failure(self):
        response = self.client.post(reverse('login_admin'), {'idNumber': 'testuser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertIn('error', response.context)


class DetalleDispositivoViewTest(TestCase):

    def setUp(self):
        self.dispositivo = Dispositivo.objects.create(
            nombre='Dispositivo de prueba',
            descripcion='Descripción del dispositivo de prueba',
            fecha_registro=timezone.now()
        )

    def test_detalle_dispositivo_view(self):
        response = self.client.get(reverse('detalle_dispositivo', args=[self.dispositivo.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detalleDispositivo.html')

    def test_detalle_dispositivo_view_context_data(self):
        response = self.client.get(reverse('detalle_dispositivo', args=[self.dispositivo.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('dispositivo' in response.context)
        self.assertEqual(response.context['dispositivo'].nombre, 'Dispositivo de prueba')


class IndexViewTest(TestCase):

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_index_view_context_data(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('title' in response.context)
        self.assertTrue('paquetes' in response.context)
        self.assertTrue('blogs' in response.context)
        self.assertEqual(response.context['title'], 'AI.Tech - Pulseras Wifi')

