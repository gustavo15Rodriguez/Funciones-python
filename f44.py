#-*-coding:utf-8-*-

'''44. Construir una función que reciba como parámetro una matriz 3x4 entera y retorne la
cantidad de veces que se repite el mayor número primo de la matriz.'''

from f42 import llenar_matriz

def encontrar_primos(matriz):
	contador = 0
	primos = []
	for g in range(len(matriz)):
		for s in range(len(matriz[g])):
			numero = matriz[g][s]
			cont = 0
			for i in range(1, numero+1):
				if numero%i==0:
					cont+=1
			if cont==2:
				primos.append(numero)
	
	return primos
	
def primo_mayor(primos):
	mayor = 0
	for i in range(len(primos)):
		if primos[i]>mayor:
			mayor = primos[i]
	return mayor	

def realizar_comparacion(primos, mayor):
	contador = 0
	for j in range(len(primos)):
		if primos[j]==mayor:
			contador+=1
	if contador>0:		
		return "El numero primo mayor en la matriz anterior se repite %d veces."%contador
	else:
		return "No habian numeros primos dentro de la matriz." 

def main():
	try:
		filas = 3
		columnas = 4 
		arreglo = llenar_matriz(filas, columnas)
		primo = encontrar_primos(arreglo)
		mayor = primo_mayor(primo)
		final = realizar_comparacion(primo, mayor)
		print final
		
	except ValueError:
		print "Error..."

if __name__ == '__main__':
	main()
