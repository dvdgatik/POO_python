# Ley de suma 

def f(n):
	for i in range(n):
		print(i)

	for i in range(n):
		print(i) 

# O(n) + O(n) = O(n+n) = O(2n) = O(n)

f(10) # crecimiento lineal

print('----------------------------------')
def f(n):

	for i in range(n):
		print(i)

	for i in range(n*n):
		print(i)

f(10) # creciemiento cuadratico 

# Ley de la multiplicacion
# 
def f(n):
	for i in range(n):
		for j in range(n):
			print(i,j)

f(10)


# recursividad multiple

def fibonacci(n):
	if n == 1:
		return 1
	if n == 0:
		return 0
	i=0
	i+=1
	print(i)
	return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(10))


