from django.test import TestCase

class ViewsTestCase(TestCase):
    def test_homepage_loads(self):
        response = self.client.get('/', follow=True)
        self.assertEqual(response.status_code, 200)
