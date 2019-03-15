#-*-coding:utf-8-*-

'''32. Construir una función que reciba como parámetro un vector de 10 posiciones enteras y
retorne el promedio real del vector.'''

from f26 import llenar_lista

def encontrar_promedio_real(lista):
	suma = 0
	cont = 0
	prom = 0
	for i in range(len(lista)):
		suma+=lista[i]
		cont+=1
	prom = float(suma//cont)
	
	return prom 
	
def main():
	try:
		elementos = 10
		vector = llenar_lista(elementos)
		promedio = encontrar_promedio_real(vector)
		print "El promedio real del vector anterior es: ",promedio
		
	except ValueError:
		print "Error..."

if __name__ == '__main__':
	main()
