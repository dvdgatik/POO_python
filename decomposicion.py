class Automovil:

	def __init__ (self, modelo, marca, color):
		self.modelo = modelo
		self.marca = marca
		self.color = color
		self._estado = 'en_reposo' # varibale privada
		self._motor = Motor(cilindros=4)

	def acelerar(self, tipo='despacio'):
		if tipo == 'rapido':
			 self._motor.inyecta_gasolina(10)
		else:
			self._motor.inyecta_gasolina(3)

		self._estado = 'en_movimiento'





class Motor:
	# tipo default keyword o parametro por defecto
	def __init__ (self, cilindros, tipo='gasolina'):
		self.cilindros = cilindros
		self.tipo = tipo
		self._temperatura = 0

	def inyecta_gasolina(self, cantidad):
		pass


class Transmision:
	def __init__(self, primera, segunda, tercera, cuarta, quinta, reversa, directa, estacionamiento, neutral)
		self.primera = primera
		self.segunda = segunda
		self.tercera = tercera
		self.cuarta = cuarta
		self.quinta = quinta
		self.reversa = reversa
		self.estacionamiento = estacionamiento
		self.neutral = neutral

	def CambiarEstandar(self, tipo='estandar')
		self.tipo.primera
		self.tipo.segunda
		self.tipo.tercera
		self.tipo.cuarta
		self.tipo.quinta
		self.tipo.reversa

	def CambiarAutomatica(self, tipo='automatica')
		self.tipo.directa
		self.tipo.reversa
		self.tipo.estacionamiento
		self.tipo.neutral






