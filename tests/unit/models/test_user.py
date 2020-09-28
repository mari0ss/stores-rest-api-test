from models.user import UserModel
from tests.unit.unit_base_test import UnitBaseTest


class UserBaseTest(UnitBaseTest):
    def test_create_user(self):
        user = UserModel('test', 'abcd')

        self.assertEqual(user.username, 'test', "initiated wrong username")
        self.assertEqual(user.password, 'abcd', "initiated wrong pass")
