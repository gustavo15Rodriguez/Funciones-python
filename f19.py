#-*-coding:utf-8-*-

'''19. Construir una función que reciba como parámetro un entero y retorne 1 si dicho valor es
un número de mínimo 3 dígitos. Deberá retornar 0 si no es así.'''

def encontrar_digitos(num):
	cont = 0
	while num>0:
		dig = num%10
		num = num//10
		cont+=1
	if cont>=3:
		return 1
	
	else:
		return 0
		
def main():
	try:
		num = int(raw_input("Digite el numero deseado: "))
		resultado = encontrar_digitos(num)
		print resultado

	except ValueError:
		print "Error..."

if __name__ == '__main__':
	main()
