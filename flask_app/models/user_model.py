from flask import Flask
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
	def __init__(self, data):
		self.id = data['id']
		self.created_at = data['created_at']
		self.updated_at = data['updated_at']