#-*-coding:utf-8-*-

'''34. Construir una función que reciba como parámetro un vector de 10 posiciones enteras y
retorne la posición del número entero que tenga mayor cantidad de dígitos.'''

from f26 import llenar_lista

def encontrar_igualdad(lista):
	mayor = 0
	for i in range(len(lista)):
		numero = lista[i]
		cont = 0
		while numero>0:
			numero//=10
			cont+=1
		
		
		if cont>mayor:
			mayor = cont
			pos = i
			
	return "La posicion exacta del numero con la mayor cantidad de digitos es: %d"%pos
		
def main():
	try:
		elementos = 10
		vector = llenar_lista(elementos)
		solucion = encontrar_igualdad(vector)
		print solucion
		
	except ValueError:
		print "Error..."

if __name__ == '__main__':
	main()
