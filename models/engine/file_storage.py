#!/usr/bin/python3
"""create class FileStorage"""

import json
from models.base_model import BaseModel


class FileStorage:
	"""class that serializes instances to a JSON file and \
	deserializes JSON file to instances"""
	__file_path = "file.json"
	__objects = {}

	def all(self):
		"""Return the dictionary __objects"""
		return FileStorage.__objects

	def new(self, obj):
		"""Sets in __objects the obj with key <obj class name>.id"""
		key = f"{obj.__class__.__name__}.{obj.id}"
		self.__objects[key] = obj

	def save(self):
		"""serializes __objects to the JSON file (path: __file_path)"""
		data = {}
		for key, obj in self.__objects.items():
			data[key] = obj.to_dict()
		with open(FileStorage.__file_path, 'w') as file:
			json.dump(data, file)

	def reload(self):
		"""deserializes the JSON file to __objects"""
		try:
			with open(FileStorage.__file_path, 'r') as file:
				data = json.load(file)
				cls_name = '__class__'
				for key, obj in data.items():
					class_name= key.split('.')
					FileStorage.__objects[key] = eval(obj[cls_name] + '(**obj)')
		except FileNotFoundError:
			return