#!/usr/bin/python3
"""create a User class"""
from models.base_model import BaseModel
import email


class User(BaseModel):
	"""Define a User"""
	email = ''
	password = ''
	first_name = ''
	last_name = ''