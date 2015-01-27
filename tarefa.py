from enums import *

class Tarefa:
	def __init__(self,titulo,descricao,data_limite,prioridade=Prioridade.baixa):
		self._titulo = titulo
		self._descricao = descricao
		self._data_limite = data_limite
		self._status = Status.pendente
		self._prioridade = prioridade

	def __str__(self):
		return self._titulo + " (" + self._prioridade + ")"

	@property
	def titulo(self):
	    return self._titulo
	@titulo.setter
	def titulo(self, value):
	    self._titulo = value

	@property
	def descricao(self):
	    return self._descricao
	@descricao.setter
	def descricao(self, value):
	    self._descricao = value

	@property
	def data_limite(self):
	    return self._data_limite
	@data_limite.setter
	def data_limite(self, value):
	    self._data_limite = value
	
	@property
	def status(self):
	    return self._status
	@status.setter
	def status(self, value):
	    self._status = value
	
	@property
	def prioridade(self):
	    return self._prioridade
	@prioridade.setter
	def prioridade(self, value):
	    self._prioridade = value