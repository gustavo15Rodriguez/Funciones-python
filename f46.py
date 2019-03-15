#-*-coding:utf-8-*-

'''46. Construir una función que reciba como parámetro una matriz 4x4 entera y retorne el
número de la fila en donde se encuentre por primera vez el número mayor de la matriz.'''

from f45 import llenar_matriz

def encontrar_mayor_en_fila(matriz):
	mayor = 0
	for g in range(len(matriz)):
		for s in range(len(matriz)):
			if matriz[g][s]>mayor:
				mayor = matriz[g][s]
				pos = g
	return pos

def main():
	try:
		filas = 4
		columnas = 4 
		arreglo = llenar_matriz(filas, columnas)
		final = encontrar_mayor_en_fila(arreglo)
		print "La fila en la que se encuentra el numero mayor es: Fila No. %d"%final

	except ValueError:
		print "Error..."

if __name__ == '__main__':
	main()
