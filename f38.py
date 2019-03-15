#-*-coding:utf-8-*-

'''38. Construir una función que reciba como parámetro un vector de 10 posiciones enteras y
retorne la cantidad de números terminados en 3 que contiene el vector.'''

from f26 import llenar_lista

def encontrar_ultimo(lista):
	cont = 0
	for i in range(len(lista)):
		if lista[i]%10==3:
			cont+=1
	return cont

def main():
	try:
		elementos = 10
		vector = llenar_lista(elementos)
		final = encontrar_ultimo(vector)
		print "Hay %d numeros que terminan en 3."%final
			
	except ValueError:
		print "Error..."

if __name__ == '__main__':
	main()
