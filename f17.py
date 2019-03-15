#-*-coding:utf-8-*-

'''17. Construir una función que reciba como parámetro un entero y retorne 1 si corresponde al
código ASCII de un dígito (Los códigos ASCII de las letras minúsculas van desde 48 que es el
código del dígito 0 hasta 57 que es el código del dígito 9). Deberá retornar 0 si no es así.'''

def encontrar_codigo(num):
	cont = 0
	if num>=48 and num <=57:
		chr(num)
		num2 = chr(num)
		cont += 1
		return cont, num2
	
	else:
		return 0
	
def main():
	try:
		num = int(raw_input("Digite el numero deseado: "))
		codigo = encontrar_codigo(num)
		print codigo

	except ValueError:
		print "Error..."

if __name__ == '__main__':
	main()
