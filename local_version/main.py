# -*- coding: utf-8 -*-

from os import system

class App:
	def __init__(self):
		self._logado = False


	def listar(self):
		pass
	def adicionar(self): 
		pass
	def remover(self): 
		pass
	def editar(self): 
		pass
	def buscar(self): 
		pass
	def logoff(self): 
		pass

	def fim(self):
		print "Pressione uma tecla para continuar...",
		t = raw_input()

	def execute(self):
		print "=== GERENCIADOR DE TAREFAS ==="
		login()
		
	def login(self):
		while not self._logado:
			print "Login:",
			login = raw_input()
			print "Senha:",
			passw = raw_input()
			pass

	def menu(self):	
		op = 0

		while op != 6:
			system("clear")

			print "=== GERENCIADOR DE TAREFAS ==="
			print "=== 1 ~> Listar Tarefas ======"
			print "=== 2 ~> Adicionar Tarefa ===="
			print "=== 3 ~> Remover Tarefa ======"
			print "=== 4 ~> Editar Tarefa ======="
			print "=== 5 ~> Buscar Tarefa ======="
			print "=== 6 ~> Logoff =============="
			print ">>>",
			op = int(raw_input())

			if op == 1:
				self.listar()
			elif op == 2:
				self.adicionar()
			elif op == 3:
				self.remover()
			elif op == 4:
				self.editar()
			elif op == 5:
				self.buscar()
			elif op == 6:
				self.logoff()
			else:
				print "Operação Inválida!"

			self.fim()



if __name__  == "__main__":
	print "OE!!!",
	op = raw_input()
	app = App()
	app.menu()