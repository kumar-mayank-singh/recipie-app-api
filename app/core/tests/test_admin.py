from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
#helper function reverse will allow us to generate the 
#urls for our django admin page

class AdminSiteTests(TestCase):

    def setUp(self):
        self.client =Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@django.com',
            password='password12@'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@dev.com',
            password='password12@'
        )