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
            password='password12@',
            name='Test user Full name'
        )

    def test_user_listed(self):
        """Test user as listed on user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_page_change(self):
        """Test that user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        #admin/core/user/1
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Tests that create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)



