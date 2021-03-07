def f(x):
	respuesta = 0

	#loop que no depende de 
	for i in range(1000): # 1000
		respuesta += 1
	#loop que depende de 
	for i in range(x):
		respuesta += x # x

	for i in range(x):
		respuesta += x

	for i in range(x):
		for j in range(x):
			respuesta += 1
			respuesta += 1 #x.x = x², 2x²


	return respuesta # 1

	# 1002 + X + 2X²
	# Los terminos que enrialidad importan son los mas grandes

