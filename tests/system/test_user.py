import json

from models.user import UserModel
from tests.base_test import BaseTest



class UserTest(BaseTest):
    def test_register_user(self):
        with self.app() as client:
            with self.app_context():
                resp = client.post('/register', data={'username': 'test', 'password': '1234'})

            self.assertEqual(resp.status_code, 201)
            self.assertIsNotNone(UserModel.find_by_username('test'))
            self.assertDictEqual(d1={'message': 'User created successfully.'},
                                     d2=json.loads(resp.data))
            


    def test_register_and_login(self):
        with self.app() as c:
            with self.app_context():
                c.post('/register', data={'username': 'test', 'password': '1234'})
                
                auth_response = c.post('/auth', data=json.dumps({
                    'username': 'test',
                    'password': '1234'
                }), headers={'Content-Type': 'application/json'})

                self.assertIn('access_token', json.loads(auth_response.data).keys())

    def test_register_duplicate_user(self):
        with self.app() as c:
            with self.app_context():
                c.post('/register',
                       data={'username': 'test', 'password': '1234'})
                r = c.post(
                    '/register', data={'username': 'test', 'password': '1234'})

                self.assertEqual(r.status_code, 400)
                self.assertDictEqual(d1={'message': 'A user with that username already exists'},
                                     d2=json.loads(r.data))
