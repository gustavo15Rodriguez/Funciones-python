#-*-coding:utf-8-*-

'''40. Construir una función que reciba como parámetro un vector de 10 posiciones enteras y
un dígito y que retorne la cantidad de números del vector que terminan en dicho dígito.'''

from f26 import llenar_lista

def encontrar_ultimo(lista, digito):
	cont = 0
	for i in range(len(lista)):
		numero = lista[i]
		dig = numero%10
		if dig == digito:
			cont+=1

	return cont
	

def main():
	try:
		elementos = 10
		vector = llenar_lista(elementos)
		digito = int(raw_input("Ingrese un numero de un digito: "))
		final = encontrar_ultimo(vector, digito)
		print "Hay %d numeros que terminan en el digito evaluado."%final

			
	except ValueError:
		print "Error..."

if __name__ == '__main__':
	main()
