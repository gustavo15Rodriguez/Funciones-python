#-*-coding:utf-8-*-

'''48. Construir una función que reciba como parámetro una matriz 4x4 entera y retorne la
posición exacta en donde se encuentre almacenado el mayor número primo.'''

from f45 import llenar_matriz

def encontrar_primo(matriz):
	primos = []
	for g in range(len(matriz)):
		for s in range(len(matriz)):
			numero = matriz[g][s]
			cont = 0
			for i in range(1, numero+1):
				if numero%i==0:
					cont+=1
			if cont==2:
				primos.append(numero)
	return primos

def encontrar_mayor_primo(primos):
	mayor = 0
	for j in range(len(primos)):
		if primos[j]>mayor:
			mayor = primos[j]
	return mayor
	
def encontrar_posicion_exacta(matriz, mayor):
	contador = 0
	posiciones = []
	for g in range(len(matriz)):
		for s in range(len(matriz)):
			if matriz[g][s]==mayor:
				contador+=1
				pos = g, s
				posiciones.append(pos)
	if contador>0:
		return "La posicion exacta del numero primo mayor en la matriz anterior es: ",posiciones
		
	else:
		return "No hay numeros primos en la matriz anterior."

def main():
	try:
		filas = 4
		columnas = 4 
		arreglo = llenar_matriz(filas, columnas)
		primo = encontrar_primo(arreglo)
		mayor = encontrar_mayor_primo(primo)
		posicion = encontrar_posicion_exacta(arreglo, mayor)
		print posicion

	except ValueError:
		print "Error..."

if __name__ == '__main__':
	main()
