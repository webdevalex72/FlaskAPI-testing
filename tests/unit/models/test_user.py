from models.user import UserModel
from tests.base_test import BaseTest


class UserTest(BaseTest):
    def test_create_user(self):
        user = UserModel('test', 'adbc')

        self.assertEqual(user.username, 'test')
        self.assertEqual(user.password, 'adbc')
