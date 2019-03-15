#-*-coding:utf-8-*-

'''20. Construir una función que reciba como parámetro un entero y retorne 1 si en dicho valor
todos los dígitos son iguales. Deberá retornar 0 si no es así.'''

def encontrar_digitos_iguales(num):
	lista = []
	cont = 0
	while num>0:
		dig = num%10
		lista.append(dig)
		num = num//10
		
	otra = lista[0]
	for g in range(len(lista)):
		if otra == lista[g]:
			cont+=1
	
	if len(lista)==cont:
		return 1
	
	else:
		return 0
		
def main():
	try:
		num = int(raw_input("Digite el numero deseado: "))
		resultado = encontrar_digitos_iguales(num)
		print resultado

	except ValueError:
		print "Error..."

if __name__ == '__main__':
	main()
