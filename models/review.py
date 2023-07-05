#!/usr/bin/python3
"""create a Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
	"""Define a Review"""
	place_id = ''
	user_id = ''
	text = ''