from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from .models import Profile


class SigninTest(TestCase):
    def setUp(self):
        self.user = Profile.objects.create(
            user= 'test',
            username='test1',
            email='test@nail.ru',
            name='tester',
        )
        # self.user = Profile.objects.create_user(username='test', password='12test12')
        self.user.save()
    def tearDown(self):
        self.user.delete()
    def test_correct(self):
        user = authenticate(username='test', password='12test12')
        self.assertTrue((user is not None) and user.is_authenticated)
    def test_wrong_username(self):
        user = authenticate(username='wrong', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated)
    def test_wrong_pssword(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)

# class LoginTest(TestCase):
#
#     def setUp(self):
#         # Создаем тестового пользователя
#         # self.user = User.objects.create_user(username='testuser', password='testpassword')
#         # self.user = get_user_model().objects.create_user(username='test',
#         #                                                  password='12test12',
#         #                                                  email='test@example.com')
#         self.user = Profile.objects.create_user(username='test', password='12test12', email='test@example.com')
#         self.user.save()
#
#     def test_login(self):
#         # Проверяем, что страница входа доступна
#         response = self.client.get(reverse('login'))
#         self.assertEqual(response.status_code, 200)
#
#         # Входим в систему
#         response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpassword'})
#         self.assertEqual(response.status_code, 302)  # Проверяем перенаправление на главную страницу
#
#         # Проверяем, что пользователь вошел в систему
#         user = authenticate(username='testuser', password='testpassword')
#         self.assertIsNotNone(user)
#         self.assertTrue(user.is_authenticated)
#
#         # Проверяем, что на главной странице видно, что пользователь вошел в систему
#         response = self.client.get(reverse('home'))
#         self.assertContains(response, 'Welcome, testuser!')
#
#     def test_logout(self):
#         # Входим в систему
#         self.client.login(username='testuser', password='testpassword')
#
#         # Проверяем, что пользователь вошел в систему
#         user = authenticate(username='testuser', password='testpassword')
#         self.assertIsNotNone(user)
#         self.assertTrue(user.is_authenticated)
#
#         # Выходим из системы
#         self.client.logout()
#
#         # Проверяем, что пользователь вышел из системы
#         user = authenticate(username='testuser', password='testpassword')
#         self.assertIsNone(user)