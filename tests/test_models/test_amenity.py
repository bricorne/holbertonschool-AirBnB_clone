#!/usr/bin/python3
"""Unit test for Amenity file"""
from models.base_model import BaseModel
from models.amenity import Amenity
import unittest


class Test_Amenity(unittest.TestCase):
    """Unit test for Amenity class"""
    def test_amenity(self):
        amenity = Amenity()
        self.assertEqual("", amenity.name)