#-*-coding:utf-8-*-

'''33. Construir una función que reciba como parámetros un vector de 10 posiciones enteras y
un valor entero y retorne 1 si dicho valor entero se encuentra en el vector. Deberá retornar 0
si no es así.'''

from f26 import llenar_lista

def encontrar_igualdad(lista, numero):
	cont = 0
	for i in range(len(lista)):
		if lista[i]==numero:
			cont+=1
			
	if cont>0:
		return 1
	
	else:
		return 0
	
def main():
	try:
		elementos = 10
		vector = llenar_lista(elementos)
		numero = int(raw_input("Digite un valor a evaluar: "))
		resultado = encontrar_igualdad(vector, numero)
		print resultado
		
	except ValueError:
		print "Error..."

if __name__ == '__main__':
	main()
