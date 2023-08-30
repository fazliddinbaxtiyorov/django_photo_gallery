from django.test import SimpleTestCase


# Create your tests here.
class SimpleTest(SimpleTestCase):
    def testing_gallery_app(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_admin(self):
        response = self.client.get('/admin')
        self.assertEqual(response.status_code, 200)