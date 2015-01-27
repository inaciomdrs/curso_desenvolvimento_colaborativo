from enum import Enum

class Status(Enum):
	pendente = 0
	iniciada = 1
	atrasada = 2
	concluida = 3

class Prioridade(Enum):
	baixa = 1
	media = 2
	alta = 3
	altissima = 4