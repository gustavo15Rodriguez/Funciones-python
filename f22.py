#-*-coding:utf-8-*-

'''22. Construir una función que reciba como parámetro un entero y retorne 1 si dicho valor es
múltiplo de 5. Deberá retornar 0 si no es así.'''

def encontrar_multiplo(num):
	if num%5==0:
		return 1
		
	else:
		return 0
		
def main():
	try:
		num = int(raw_input("Digite el numero deseado: "))
		resultado = encontrar_multiplo(num)
		print resultado

	except ValueError:
		print "Error..."

if __name__ == '__main__':
	main()
