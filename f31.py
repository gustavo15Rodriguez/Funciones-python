#-*-coding:utf-8-*-

'''31. Construir una función que reciba como parámetro un vector de 10 posiciones enteras y
retorne el promedio entero del vector.'''

from f26 import llenar_lista

def encontrar_promedio(lista):
	suma = 0
	cont = 0
	prom = 0
	for i in range(len(lista)):
		suma+=lista[i]
		cont+=1
	prom = suma//cont
	
	return prom 
	
def main():
	try:
		elementos = 10
		vector = llenar_lista(elementos)
		promedio = encontrar_promedio(vector)
		print "El promedio entero del vector anterior es: ",promedio
		
	except ValueError:
		print "Error..."

if __name__ == '__main__':
	main()
