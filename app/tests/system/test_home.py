# app/tests/system/test_home.py
from tests.system.base_test import BaseTest
import json


class TestHome(BaseTest):
    def test_home(self):
        """Testing home page of webapp"""
        with self.app() as client:
            response = client.get('/')

            self.assertEqual(response.status_code, 200)
            self.assertDictEqual(
                json.loads(response.get_data()),
                {'message': 'Hello World!'}
            )
