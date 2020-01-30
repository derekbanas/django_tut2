from django.test import SimpleTestCase

class LinkTests(SimpleTestCase):
    def test_home_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_status_code(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)
