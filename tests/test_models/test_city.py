#!/usr/bin/python3
"""Unit test for City file"""
from models.base_model import BaseModel
from models.city import City
import unittest


class Test_City(unittest.TestCase):
    """Unit test for City class"""
    def test_city(self):
        city = City()
        self.assertEqual("", city.name)
        self.assertEqual("", city.state_id)