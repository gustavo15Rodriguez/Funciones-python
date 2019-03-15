#-*-coding:utf-8-*-

'''27. Construir una función que reciba como parámetro un vector de 10 posiciones enteras y
retorne la posición en la cual se encuentra el mayor de los datos del vector.'''

from f26 import llenar_lista

def encontrar_posicion_dato_mayor(lista):
	mayor = 0
	for g in range(len(lista)):
		if lista[g]>mayor:
			mayor = lista[g]
			
	posicion = []		
	for s in range(len(lista)):
		if mayor == lista[s]:
			pos = s
			posicion.append(pos)
	return posicion
		
def main():
	try:
		elementos = 10
		vector = llenar_lista(elementos)
		posiciones_mayor = encontrar_posicion_dato_mayor(vector)
		print "La posicion exacta del dato mayor en el vector anterior es: ",posiciones_mayor
		
	except ValueError:
		print "Error..."

if __name__ == '__main__':
	main()
