#-*-coding:utf-8-*-

'''15. Construir una función que reciba como parámetros dos números enteros y retorne 1 si el
primer número es múltiplo del segundo y 0 si no.'''

def encontrar_multiplo(num1, num2):
	if num1%num2==0:
		return 1
		
	else:
		return 0

def main():
	try:
		num1 = int(raw_input("Digite el primer numero: "))
		num2 = int(raw_input("Digite el segundo numero: "))
		multiplo = encontrar_multiplo(num1, num2)
		print multiplo

	except ValueError:
		print "Error..."

if __name__ == '__main__':
	main()
