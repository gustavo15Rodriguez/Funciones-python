#-*-coding:utf-8-*-

'''3. Construir una función que reciba como parámetro un entero y retorne la cantidad de
dígitos.'''

def cantidad_digitos(num):
	cont = 0
	while num>0:
		dig = num%10
		num = num//10
		cont+=1
		
	return cont

def main():
	try:
		num = int(raw_input("Digite el elemento deseado: "))
		total = cantidad_digitos(num)
		print "La cantidad de digitos del numero anterior es: ",total
		
				
	except ValueError:
		print "Error..."
		
if __name__ == '__main__':
	main()
