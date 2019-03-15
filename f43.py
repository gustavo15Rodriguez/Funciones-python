#-*-coding:utf-8-*-

'''43. Construir una función que reciba como parámetro una matriz 3x4 entera y retorne la
cantidad de números primos almacenados en la matriz.'''

from f42 import llenar_matriz

def encontrar_primos(matriz):
	contador = 0
	for g in range(len(matriz)):
		for s in range(len(matriz[g])):
			numero = matriz[g][s]
			cont = 0
			for i in range(1, numero+1):
				if numero%i==0:
					cont+=1
			if cont==2:
				contador+=1
	
	return contador
	
def main():
	try:
		filas = 3
		columnas = 4 
		arreglo = llenar_matriz(filas, columnas)
		primo = encontrar_primos(arreglo)
		print "Hay %d numeros primos dentro de la matriz anterior."%primo
		
	except ValueError:
		print "Error..."

if __name__ == '__main__':
	main()
