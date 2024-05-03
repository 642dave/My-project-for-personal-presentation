import unittest
import sys
sys.path.append('C:\\Users\\Dave\\Desktop\\Programovani\\My Casino project\\My-project-for-personal-presentation\\python')
from app import app

class TestRegistration(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_registration_success(self):
        data = {
            'name': 'John',
            'surname': 'Doe',
            'nickname': 'johndoe',
            'age': '30',
            'email': 'john@example.com',
            'password': 'password123'
        }
        response = self.app.post('/registry', data=data, follow_redirects=True)
        self.assertIn(b'Registration successful!', response.data)

    def test_registration_failure(self):
        data = {
            'name': 'John',
            'surname': 'Doe',
            'nickname': 'johndoe',
            'age': '30',
            'email': 'john@example.com',
            'password': ''  # invalid password
        }
        response = self.app.post('/registry', data=data, follow_redirects=True)
        self.assertIn(b'Registration failed!', response.data)

class TestLogin(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_login_success(self):
        data = {
            'email': 'john@example.com',
            'password': 'password123'
        }
        response = self.app.post('/', data=data, follow_redirects=True)
        self.assertIn(b'Welcome johndoe!', response.data)

    def test_login_failure(self):
        data = {
            'email': 'john@example.com',
            'password': 'wrongpassword'  # invalid password
        }
        response = self.app.post('/', data=data, follow_redirects=True)
        self.assertIn(b'Login incorrect', response.data)

class TestLogout(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_logout(self):
        response = self.app.get('/logout', follow_redirects=True)
        self.assertNotIn(b'Welcome', response.data)  # User should not be logged in after logout

if __name__ == '__main__':
    unittest.main()



