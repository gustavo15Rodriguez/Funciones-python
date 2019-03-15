#-*-coding:utf-8-*-

'''18. Construir una función que reciba como parámetro un valor entero y un digito, retornar 1
si dicho valor es el factorial de alguno del dígito ingresado. Deberá retornar 0 si no es así.'''

def encontrar_factorial(num, dig):
	factorial = 1
	for i in range(1, dig+1):
		factorial = factorial * i
	if factorial == num:
		return 1
		
	else:
		return 0
	
def main():
	try:
		num = int(raw_input("Digite el numero deseado: "))
		dig = int(raw_input("Ingrese el digito deseado: "))
		resultado = encontrar_factorial(num, dig)
		print resultado

	except ValueError:
		print "Error..."

if __name__ == '__main__':
	main()
