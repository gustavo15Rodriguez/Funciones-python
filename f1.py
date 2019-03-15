#-*-coding:utf-8-*-

'''1. Construir una función que reciba como parámetro un entero y retorne su último dígito.'''

def ultimo_digito(num):
	dig = num%10
	return dig

def main():
	try:
		num = int(raw_input("Digite el elemento deseado: "))
		ultimo = ultimo_digito(num)
		print "El ultimo numero del dato evaluado es: ",ultimo
		
	except ValueError:
		print "Error..."
		
if __name__ == '__main__':
	main()
