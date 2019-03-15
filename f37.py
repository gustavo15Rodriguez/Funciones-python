#-*-coding:utf-8-*-

'''37. Construir una función que reciba como parámetros dos enteros, el primero actuará como
base y el segundo como exponente y retorne el resultado de elevar dicha base a dicho
exponente.'''

def encontrar_resultado(num1, num2):
	factorial = 1
	for a in range(0, num2):
		factorial = factorial*num1
	return factorial

def main():
	try:
		num1 = int(raw_input("Digite el numero base de la operacion: "))
		num2 = int(raw_input("Digite el numero exponente de la operacion: "))
		solucion = encontrar_resultado(num1, num2)
		print "El resultado de elevar %d"%num1 + " por %d"%num2 + " es:",solucion
		
	except ValueError:
		print "Error..."

if __name__ == '__main__':
	main()
