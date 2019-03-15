#-*-coding:utf-8-*-

'''14. Construir una función que reciba como parámetros dos números enteros y retorne el
valor del mayor.'''

def encontrar_mayor(num1, num2):
	if num1>num2:
		return "El numero mayor es: %d"%num1
		
	else:
		return "El numero mayor es: %d"%num2

def main():
	try:
		num1 = int(raw_input("Digite el primer numero: "))
		num2 = int(raw_input("Digite el segundo numero: "))
		mayor = encontrar_mayor(num1, num2)
		print mayor
		
	except ValueError:
		print "Error..."

if __name__ == '__main__':
	main()
