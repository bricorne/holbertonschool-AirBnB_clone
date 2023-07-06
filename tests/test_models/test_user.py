#!/usr/bin/python3
"""Unit test for User file"""
from models.base_model import BaseModel
from models.user import User
import email
import unittest


class Test_User(unittest.TestCase):
    """Unit test for User class"""
    def test_user(self):
        user = User
        self.assertEqual("", user.email)
        self.assertEqual("", user.password)
        self.assertEqual("", user.first_name)
        self.assertEqual("", user.last_name)