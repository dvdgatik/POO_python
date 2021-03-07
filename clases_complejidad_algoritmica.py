import math
import time

class Complejidad_algoritmica:

	def __init__(self, n):
		self.n = n

	def constante(self):
		return 1

	def lineal(self):
		return self.n

	def logaritmica(self):
		return math.log10(self.n)

	def log_lineal(self):
		return self.n * (math.log10(self.n))

	def polinominal(self):
		return self.n ** 2

	def exponencial(self):
		return 2**self.n



n = int(input('Ingresa el valor de n: '))
complejidad = Complejidad_algoritmica(n)

print(f'Constante: {complejidad.constante()}')

print(f'Lineal: {complejidad.lineal()}')

print(f'Logaritmica: {complejidad.logaritmica()}')

print(f'Logaritmica Lineal:  {complejidad.log_lineal()}')

print(f'Polinominal: {complejidad.polinominal()}')

print(f'Exponencial: {complejidad.exponencial()}')








