#-*-coding:utf-8-*-

'''45. Construir una función que reciba como parámetros una matriz 4x4 entera y un valor
entero y retorne la cantidad de veces que se repite dicho valor en la matriz.'''

def llenar_matriz(filas, columnas):
	matriz = []
	for i in range(filas):
		fila = []
		for j in range(columnas):
			num = int(raw_input("Digite el numero deseado: "))
			fila.append(num)
		matriz.append(fila)
	return matriz

def comparar_datos(matriz, num2):
	cont = 0
	for g in range(len(matriz)):
		for s in range(len(matriz)):
			if matriz[g][s]==num2:
				cont+=1
	return cont

def main():
	try:
		filas = 4
		columnas = 4 
		arreglo = llenar_matriz(filas, columnas)
		num2 = int(raw_input("Digite el numero a evaluar: "))
		final = comparar_datos(arreglo, num2)
		print "El numero evaluado se repite %d veces en la matriz anterior."%final
	
	except ValueError:
		print "Error..."

if __name__ == '__main__':
	main()
