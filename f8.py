#-*-coding:utf-8-*-

'''8. Construir una función que reciba como parámetro un entero y retorne 1 si dicho entero
está entre los 30 primeros elementos de la serie de Fibonacci. Deberá retornar 0 si no es así.'''

def encontrar_fibonacci(num):
	numero = 1
	ultimo = 0
	penultimo = 0
	fibonacci = []
	for i in range(31):
		penultimo = ultimo
		ultimo = numero
		numero = penultimo+ultimo
		fibonacci.append(numero)
	
	return fibonacci

def comparar(num, fibonacci):
	cont = 0
	for i in range(len(fibonacci)):
		if fibonacci[i]==num:
			cont+=1
	
	if cont!=0 or num == 0:
		return 1
	
	else:
		return 0
	
def main():
	try:
		num = int(raw_input("Digite el elemento deseado: "))
		fibonacci = encontrar_fibonacci(num)
		final = comparar(num, fibonacci)
		print final
	
	except ValueError:
		print "Error..."
		
if __name__ == '__main__':
	main()
