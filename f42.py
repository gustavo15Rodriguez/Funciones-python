#-*-coding:utf-8-*-

'''42. Construir una función que reciba como parámetro una matriz de 3x4 entera y retorne la
cantidad de veces que se repite el mayor dato de la matriz.'''

def llenar_matriz(filas, columnas):
	matriz = []
	for i in range(filas):
		filas = []
		for j in range(columnas):
			num = int(raw_input("Digite el numero deseado: "))
			filas.append(num)
		matriz.append(filas)
		
	return matriz
	
def encontrar_mayor(matriz):
	mayor = 0
	for g in range(len(matriz)):
		for s in range(len(matriz[g])):
			if matriz[g][s]>mayor:
				mayor = matriz[g][s]
	return mayor

def encontrar_repetido(matriz, mayor):
	cont = 0
	for a in range(len(matriz)):
		for b in range(len(matriz[a])):
			if matriz[a][b]==mayor:
				cont+=1
	return cont
	
def main():
	try:
		filas = 3
		columnas = 4 
		arreglo = llenar_matriz(filas, columnas)
		dato = encontrar_mayor(arreglo)
		total = encontrar_repetido(arreglo, dato)
		print "El numero mayor de la matriz se repite %d veces en la misma."%total
			
	except ValueError:
		print "Error..."

if __name__ == '__main__':
	main()
