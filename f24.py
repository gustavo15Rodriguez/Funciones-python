#-*-coding:utf-8-*-

'''24. Construir una función que reciba como parámetro dos enteros de dos dígitos cada uno y
retorne 1 si son inversos. Ejemplo: 83 es inverso de 38. Deberá retornar 0 si no es así.'''

def encontrar_inverso(num1, num2):
	if num1>0 and num1<=99 and num2>0 and num2<=99:
		dig1 = num1%10
		num1 = num1//10
		
		dig2 = num2%10
		num2 = num2//10
		
		if num1==dig2 and dig1==num2:
			return 1
		
		else:
			return 0
	else:
		return "Los numeros ingresados deben ser de dos digitos cada uno."
	
def main():
	try:
		num1 = int(raw_input("Digite el primer numero de dos digitos: "))
		num2 = int(raw_input("Digite el segundo numero de dos digitos: "))
		inverso = encontrar_inverso(num1, num2)
		print inverso

	except ValueError:
		print "Error..."

if __name__ == '__main__':
	main()
