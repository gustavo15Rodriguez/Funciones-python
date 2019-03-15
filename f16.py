#-*-coding:utf-8-*-

'''16. Construir una función que reciba como parámetro un entero y retorne 1 si corresponde al
código ASCII de una letra minúscula (Los códigos ASCII de las letras minúsculas van desde 97
que el código de la letra a hasta 122 que es el código de la letra z). Deberá retornar 0 si no es
así.'''

def encontrar_codigo(num):
	cont = 0
	if num>=97 and num <=122:
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
