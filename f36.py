#-*-coding:utf-8-*-

'''36. Construir una función que reciba como parámetro un entero y retorne ese elemento de
la serie de Fibonacci.'''

def encontrar_fibonacci(num):
	numero = 1
	ultimo = 0
	penultimo = 0
	fibonacci = [0,1]
	for i in range(num):
		penultimo = ultimo
		ultimo = numero
		numero = penultimo+ultimo
		fibonacci.append(numero)
	return fibonacci

def evaluar_elementos(num, fibonacci):
	numero = 0
	for g in range(num):
		for s in range(len(fibonacci)):
			if g == s:
				numero = fibonacci[s]
		numero = numero
	
	return numero
	
def main():
	try:
		num = int(raw_input("Digite el numero deseado: "))
		vector = encontrar_fibonacci(num)
		total = evaluar_elementos(num, vector)
		print "El numero fibonacci equivalente al numero ingresado es: ",total
		
	except ValueError:
		print "Error..."

if __name__ == '__main__':
	main()
