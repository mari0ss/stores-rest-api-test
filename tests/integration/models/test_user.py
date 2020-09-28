from models.user import UserModel
from tests.base_test import BaseTest


class TestUser(BaseTest):
    def test_crud(self):
        with self.app_context():
            user = UserModel('user','abcd')

            self.assertIsNone(user.find_by_username('user'))
            self.assertIsNone(user.find_by_id(1))

            user.save_to_db()

            self.assertIsNotNone(user.find_by_username('user'))
            self.assertIsNotNone(user.find_by_id(1))