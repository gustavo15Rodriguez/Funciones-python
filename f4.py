#-*-coding:utf-8-*-

'''4. Construir una función que reciba como parámetro un entero y retorne la cantidad de
dígitos pares.'''

def cantidad_digitos_pares(num):
	cont = 0
	while num>0:
		dig = num%10
		if dig%2==0:
			cont+=1
		num = num//10
	return cont

def main():
	try:
		num = int(raw_input("Digite el elemento deseado: "))
		total = cantidad_digitos_pares(num)
		print "La cantidad de digitos pares del numero anterior es: ",total
			
	except ValueError:
		print "Error..."
		
if __name__ == '__main__':
	main()
