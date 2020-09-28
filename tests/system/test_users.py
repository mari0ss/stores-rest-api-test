from models.user import UserModel
from tests.base_test import BaseTest
import json

class TestUser(BaseTest):
    def test_registration(self):
        with self.app() as client:
            with self.app_context():
                response = client.post("/register", data = {'username':'test', 'password':'1234'})
                print (f"response: {response.data} {response.status_code}")
                self.assertEqual(response.status_code, 201)
                self.assertIsNotNone(UserModel.find_by_username('test'))
                self.assertDictEqual(json.loads(response.data), {'message':'User created successfully'})

    def test_registration_login(self):
        with self.app() as client:
            with self.app_context():
                client.post("/register", data = {'username':'test', 'password':'1234'})
                auth_response= client.post("/auth",
                                           data = json.dumps({'username':'test', 'password':'1234'}),
                                           headers= {'Content-Type': 'application/json'})
                self.assertIn('access_token', json.loads(auth_response.data).keys())

    def test_duplicate_user(self):
        with self.app() as client:
            with self.app_context():
                client.post("/register", data={'username': 'test', 'password': '1234'})
                response = client.post("/register", data={'username': 'test', 'password': '1234'})
                print(f"response: {response.data} {response.status_code}")

                self.assertEqual(response.status_code, 400)
                self.assertIsNotNone(UserModel.find_by_username('test'))
                self.assertDictEqual(json.loads(response.data), {'message': 'A user with this username already exists'})