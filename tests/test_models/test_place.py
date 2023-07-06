#!/usr/bin/python3
"""Unit test for Place file"""
from models.base_model import BaseModel
from models.place import Place
import unittest


class Test_Place(unittest.TestCase):
    """Unit test for Place class"""
    def test_place(self):
        pl = Place()
        self.assertEqual('', pl.name)
        self.assertEqual(0, pl.number_rooms)