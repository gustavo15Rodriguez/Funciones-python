#-*-coding:utf-8-*-

'''11. Construir una función que reciba como parámetro un entero y un dígito y retorne 1 si
dicho entero es múltiplo de dicho dígito y 0 si no es así.'''

def encontrar_multiplo(num, dig):
	if num%dig==0:
		return 1
	
	else:
		return 0

def main():
	try:
		num = int(raw_input("Digite el numero deseado: "))
		dig = int(raw_input("Digite el digito deseado: "))
		multiplo = encontrar_multiplo(num, dig)
		print multiplo

		
	except ValueError:
		print "Error..."

if __name__ == '__main__':
	main()
