import time
# Comparación de tiempo con implementación recusriva vs iterativa
def factorial(n):
	respuesta = 1

	while n >  1:
		respuesta *= n # respuesta = respuesta * n
		n -= 1  # n = n -1

	return respuesta 


def factorial_r(n):
	if n == 1:
		return 1

	return n * factorial(n-1)


if __name__ == '__main__':
	n = 200000

	comienzo = time.time() #modulo.funcion()
	factorial(n)
	final = time.time()
	print('Con ciclo: ' + str(final - comienzo))


	comienzo =  time.time()
	factorial_r(n)
	final = time.time()
	print('Con recursividad: ' + str(final - comienzo))

