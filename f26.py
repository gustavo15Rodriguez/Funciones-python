#-*-coding:utf-8-*-

'''26. Construir una función que reciba como parámetro un vector de 10 posiciones enteras y
retorne el mayor de los datos del vector.'''

def llenar_lista(elementos):
	lista = []
	for i in range(elementos):
		num = int(raw_input("Digite el numero deseado: "))
		lista.append(num)
	return lista

def encontrar_mayor(lista):
	mayor = 0
	for g in range(len(lista)):
		if lista[g]>mayor:
			mayor = lista[g]
	return mayor
		
def main():
	try:
		elementos = 10
		vector = llenar_lista(elementos)
		numero_mayor = encontrar_mayor(vector)
		print "El dato mayor de vector anterior es: ",numero_mayor
		
	except ValueError:
		print "Error..."

if __name__ == '__main__':
	main()
