#!/usr/bin/python3
"""Unit test for Review file"""
from models.base_model import BaseModel
from models.review import Review
import unittest


class Test_Review(unittest.TestCase):
    """Unit test for Review class"""
    def test_review(self):
        review = Review
        self.assertEqual("", review.place_id)
        self.assertEqual("", review.user_id)
        self.assertEqual("", review.text)