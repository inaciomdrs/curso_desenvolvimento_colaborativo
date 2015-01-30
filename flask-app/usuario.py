from flask.ext.sqlalchemy import SQLAlchemy
from tarefa import Tarefa

class Usuario:
	contador_de_codigos = 1

	def __init__(self,login,senha,email):
		self._cod = contador_de_codigos
		self._login = login
		self._senha = senha
		self._email = email
		self._tarefas = []

		contador_de_codigos += 1

	def __str__(self):
		return self._login + " (" + self._email + ")"

	@property
	def cod(self):
	    return self._cod

	@property
	def tarefas(self):
	    return self._tarefas
	
	@property
	def login(self):
	    return self._login
	@login.setter
	def login(self, value):
	    self._login = value
	
	@property
	def senha(self):
	    return self._senha
	@senha.setter
	def senha(self, value):
	    self._senha = value
	
	@property
	def email(self):
	    return self._email
	@email.setter
	def email(self, value):
	    self._email = value