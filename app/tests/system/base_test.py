# app/tests/system/base_test.py
"""This module create a root point for nesting UnitTests"""
from unittest import TestCase
from app import app


class BaseTest(TestCase):
    def setUp(self) -> None:
        app.testing = True  # this is for Flask app Exeptions, Errors
        self.app = app.test_client
