#!/usr/bin/python3
"""Unit test for State file"""
from models.base_model import BaseModel
from models.state import State
import unittest


class Test_State(unittest.TestCase):
    """Unit test for State class"""
    def test_name(self):
        state = State()
        self.assertEqual("", state.name)