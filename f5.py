#-*-coding:utf-8-*-

'''5. Construir una función que reciba como parámetro un entero y retorne la cantidad de
dígitos primos.'''

def cantidad_digitos_primos(num):
	cont2 =0
	while num>0:
		cont = 0
		dig = num%10
		for j in range(1, dig+1):
			if dig%j==0:
				cont+=1
		if cont==2:
			cont2+=1
		num = num//10
	return cont2

def main():
	try:
		num = int(raw_input("Digite el numero deseado: "))
		total = cantidad_digitos_primos(num)
		print "La cantidad de digitos primos del numero anterior es: ",total
			
	except ValueError:
		print "Error..."
		
if __name__ == '__main__':
	main()
