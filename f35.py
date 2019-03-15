#-*-coding:utf-8-*-

'''35. Construir una función que reciba como parámetro un vector de 10 posiciones enteras y
retorne la posición en la que se encuentre el mayor número primo que termine en 3
almacenado en el vector.'''

from f26 import llenar_lista

def encontrar_primos(lista):
	primos = []
	for s in range(len(lista)):
		num = lista[s]
		cont = 0
		for g in range(1, num+1):
			if num%g==0:
				cont+=1
		if cont==2:
			primos.append(num)
	
	return primos

def encontrar_primo_terminado(primos):
	final = []
	for i in range(len(primos)):
		num = primos[i]
		if num%10==3:
			final.append(num)
	
	return final
			
def encontrar_primo_mayor(final):	
	mayor = 0
	for j in range(len(final)):
		if final[j]>mayor:
			mayor = final[j]
	
	return mayor		

def encontrar_posicion(mayor, lista):
	posiciones = []
	cont = 0
	for g in range(len(lista)):
		if lista[g]==mayor:
			cont+=1
			pos = g
			posiciones.append(pos)
			
	if cont>0:
		return posiciones
		
	else:
		return "No hay numeros primos terminados en 3."  

def main():
	try:
		elementos = 10
		vector = llenar_lista(elementos)
		primos = encontrar_primos(vector)
		ultimo = encontrar_primo_terminado(primos)
		mayor = encontrar_primo_mayor(ultimo)
		resultado = encontrar_posicion(mayor, vector)
		print "La posicion exacta donde se encuentra el mayor numero primo terminado en 3 es: ",resultado
		
	except ValueError:
		print "Error..."

if __name__ == '__main__':
	main()
