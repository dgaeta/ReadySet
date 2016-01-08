# ReadySet/models.py

from ReadySet import app 
from ReadySet import db
from passlib.apps import custom_app_context as pwd_context

class User(db.Model):

	__tablename__ = 'user'

	# Columns
	id = db.Column(db.Integer, primary_key = True)
 	username = db.Column(db.String(32), index = True)
 	password_hash = db.Column(db.String(128))
	first_name = db.Column(db.String(128))
	last_name = db.Column(db.String(128))
	authenticated = db.Column(db.Boolean, default=False)

	# Helper methods 

	def __init__(self, username, first_name, last_name):
		self.username = str(username) 
		self.first_name = str(first_name)
		self.last_name = str(last_name)

	def __repr__(self):
		return "User {0} {1} {2}".format(self.username, self.first_name, self.last_name)

	# Required methods for Flask-login-UserMixin

	def is_active(self):
 		"""True, as all users are active."""
 		return True

	def get_id(self):
 		"""Return the username to satisfy Flask-Login's requirements."""
 		return self.username

	def is_authenticated(self):
 		"""Return True if the user is authenticated."""
 	 	return self.authenticated

	def is_anonymous(self):
 		"""False, as anonymous users aren't supported."""
 		return False

	def hash_password(self, password):
 	 	self.password_hash = pwd_context.encrypt(password)

 	def verify_password(self, password):
		return pwd_context.verify(password, self.password_hash)

