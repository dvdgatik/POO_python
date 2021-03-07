class Rectangulo:

	def __init__(self, base, altura): #variables de instancia
		self.base = base
		self.altura = altura

	def area(self):
		return self.base * self.altura


#extends
class Cuadrado(Rectangulo):

	def __init__(self, lado):
		super().__init__(lado, lado) #obtener una referencia directa de la superclase y poder llamar a su constructor


if __name__ == '__main__':
	rectangulo = Rectangulo(base=3, altura=4)
	cuadrado = Cuadrado(lado=5)

	print(f'El area del rectangulo es:  {rectangulo.area()}')
	print(f'EL area del cuadrado es: ' + str(cuadrado.area()))


