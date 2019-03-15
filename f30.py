#-*-coding:utf-8-*-

'''30. Construir una función que reciba como parámetro un vector de 10 posiciones enteras y
retorne la posición del mayor número primo almacenado en el vector.'''

from f26 import llenar_lista

def encontrar_primos(lista):
	primo = []
	for i in range(len(lista)):
		numero = lista[i]
		cont = 0
		for j in range(1, numero+1):
			if numero%j == 0:
				cont +=1
		if cont==2:
			primo.append(numero)
	return primo

def encontrar_primo_mayor(primo):
	mayor = 0
	for i in range(len(primo)):
		if primo[i]>mayor:
			mayor = primo[i]
	
	return mayor

		
def encontrar_posicion_exacta(lista, mayor):
	posiciones = []
	for g in range(len(lista)):
		if lista[g]==mayor:
			pos = g
			posiciones.append(pos)
	return posiciones
		
def main():
	try:
		elementos = 10
		vector = llenar_lista(elementos)
		primos = encontrar_primos(vector)
		mayor = encontrar_primo_mayor(primos)
		posicion = encontrar_posicion_exacta(vector, mayor)
		print "La posicion exacta del numero primo mayor en el vector anterior es: ",posicion
		
	except ValueError:
		print "Error..."

if __name__ == '__main__':
	main()
