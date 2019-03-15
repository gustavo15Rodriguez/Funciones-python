#-*-coding:utf-8-*-

'''28. Construir una función que reciba como parámetro un vector de 10 posiciones enteras y
retorne la cantidad de números primos almacenados en el vector.'''

from f26 import llenar_lista

def encontrar_cantidad_primos(lista):
	contador = 0
	for s in range(len(lista)):
		num = lista[s]
		cont = 0
		for g in range(1, num+1):
			if num%g==0:
				cont+=1
		if cont==2:
			contador+=1
				
	return contador
		
def main():
	try:
		elementos = 10
		vector = llenar_lista(elementos)
		cantidad_primos = encontrar_cantidad_primos(vector)
		print "Hay %d numeros primos en el vector anterior."%cantidad_primos

		
	except ValueError:
		print "Error..."

if __name__ == '__main__':
	main()
