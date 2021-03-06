# Ejemplo clase persona


# Definición

class Persona:
	#Atributos
	def __init__ (self, nombre, edad):
		#variables de instancia self.nombre_variable
		self.nombre = nombre
		self.edad = edad
	#Metodos
	def saluda(self, otra_persona):
		return f'Hola {otra_persona.nombre} me llamo {self.nombre}.'



#Uso
#Inicializar dos instancias de la clase
david = Persona('David',35)
erika = Persona('Erika',32)

#Con dot notation ejecutamos los métodos de esa clase directamente en la instancia
david.saluda(erika)


print(david)
print(erika)
print(david.saluda(erika))



