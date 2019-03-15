#-*-coding:utf-8-*-

'''39. Construir una función que reciba como parámetros un vector de 10 posiciones enteras y
un dígito y que retorne la cantidad de veces que dicho dígito se encuentra en el vector. No se
olvide que un mismo dígito puede estar varias veces en un solo número.'''

from f26 import llenar_lista

def encontrar_ultimo(lista, digito):
	cont = 0
	for i in range(len(lista)):
		numero = lista[i]
		while numero>0:
			dig = numero%10
			if dig == digito:
				cont+=1
			numero = numero//10
	
	return cont
	

def main():
	try:
		elementos = 10
		vector = llenar_lista(elementos)
		digito = int(raw_input("Ingrese un numero de un digito: "))
		final = encontrar_ultimo(vector, digito)
		print "El digito ingresado se repite %d veces en el vector anterior."%final

			
	except ValueError:
		print "Error..."

if __name__ == '__main__':
	main()
