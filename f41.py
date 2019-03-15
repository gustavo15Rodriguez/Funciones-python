#-*-coding:utf-8-*-

'''41. Construir una función que reciba como parámetro un vector de 10 posiciones enteras y
un dígito y que retorne la cantidad de números del vector en donde dicho dígito está de
penúltimo.'''

from f26 import llenar_lista

def encontrar_penultimo(lista, digito):
	cont = 0
	for i in range(len(lista)):
		numero = lista[i]
		numero = numero//10
		dig = numero%10
		if dig == digito:
			cont+=1

	return cont
	
def main():
	try:
		elementos = 10
		vector = llenar_lista(elementos)
		digito = int(raw_input("Ingrese un numero de un digito: "))
		final = encontrar_penultimo(vector, digito)
		print "Hay %d numeros cuyo penultimo digito es igual al digito evaluado."%final

			
	except ValueError:
		print "Error..."

if __name__ == '__main__':
	main()
