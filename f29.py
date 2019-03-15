#-*-coding:utf-8-*-

'''29. Construir una función que reciba como parámetro un vector de 10 posiciones enteras y
retorne la cantidad de números que pertenecen a los 30 primeros elementos de la serie de
Fibonacci.'''

from f26 import llenar_lista

def encontrar_fibonacci(lista):

	fibonacci = [0]
	numero = 1
	penultimo = 0
	ultimo = 0
	for s in range(31):
		penultimo = ultimo
		ultimo = numero
		numero = penultimo + ultimo
		fibonacci.append(numero)
			
	return fibonacci
	
def encontrar_cantidad_fibonacci(lista, fibonacci):
	contador = 0
	for g in range(len(lista)):
		num = lista[g]
		for s in range(len(fibonacci)):
			if fibonacci[s]==num:
				contador+=1
	
	return contador
		
def main():
	try:
		elementos = 10
		vector = llenar_lista(elementos)
		fibonacci = encontrar_fibonacci(vector)
		total = encontrar_cantidad_fibonacci(vector, fibonacci)
		print "Hay %d numeros que pertenecen a la serie fibonacci."%total
		
	except ValueError:
		print "Error..."

if __name__ == '__main__':
	main()
