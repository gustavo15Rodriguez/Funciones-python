#-*-coding:utf-8-*-

'''10. Construir una función que reciba como parámetro un entero y retorne el primer dígito de
este entero.'''

def encontrar_primer_digito(num):
	while num>0:
		dig = num%10
		num = num//10
	return dig

def main():
	try:
		num = int(raw_input("Digite el numero deseado: "))
		digito = encontrar_primer_digito(num)
		print "El primer digito del numero evaluado es: ",digito
		
	except ValueError:
		print "Error..."

if __name__ == '__main__':
	main()
