class Lavadora:

	def __init__(self):
		pass

	def lavar(self, temperatura='Fria'):
		self._llenar_tanque_agua(temperatura)
		self._anadir_jabon()
		self._lavar() #metodo distinto privado
		self._centrifugar()

	def _llenar_tanque_agua (self, temperatura):
		print(f'Llenando el tanque con agua {temperatura}')

	def _anadir_jabon(self):
		print(f'Añadiendo Jabon')
	
	def _lavar(self):
		print('Lavando la ropa')

	def _centrifugar(self):
		print(f'Centrifugando la ropa')



if __name__ == '__main__':
	lavadora = Lavadora()
	lavadora.lavar()