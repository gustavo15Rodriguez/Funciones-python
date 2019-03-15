#-*-coding:utf-8-*-

'''21. Construir una función que reciba como parámetro un entero y retorne 1 si en dicho valor
el primer dígito es igual al último. Deberá retornar 0 si no es así.'''

def encontrar_coincidencia(num):
	ultimo_digito = num%10
	cont = 0
	while num>0:
		dig = num%10
		if num == ultimo_digito:
			cont+=1
		num = num//10
	if cont>0:
		return 1
		
	else:
		return 0
		
def main():
	try:
		num = int(raw_input("Digite el numero deseado: "))
		resultado = encontrar_coincidencia(num)
		print resultado

	except ValueError:
		print "Error..."

if __name__ == '__main__':
	main()
