#-*-coding:utf-8-*-

'''9. Construir una función que reciba un entero y le calcule su factorial sabiendo que el
factorial de un número es el resultado de multiplicar sucesivamente todos los enteros
comprendidos entre 1 y el número dado. El factorial de 0 es 1. No están definidos los
factoriales de números negativos.'''

def encontrar_factorial(num):
	if num>=0:	
		factorial = 1
		for g in range(1, num+1):
			factorial = factorial * g

		return factorial
		
	else:
		return "El numero ingresado es negativo"

def main():
	try:
		num = int(raw_input("Digite el numero deseado: "))
		factorial = encontrar_factorial(num)
		print factorial
	
	except ValueError:
		print "Error..."

if __name__ == '__main__':
	main()
