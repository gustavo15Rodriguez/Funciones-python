#-*-coding:utf-8-*-

'''2. Construir una función que reciba como parámetro un entero y retorne sus dos últimos
dígitos.'''

def ultimo_digito(num):
	dig = num%10
	return dig
	
def penultimo_digito(num):
	num = num//10
	dig = num%10
	
	return dig


def main():
	try:
		num = int(raw_input("Digite el elemento deseado: "))
		ultimo = ultimo_digito(num)
		penultimo = penultimo_digito(num)
		print "El ultimo digito del numero evaluado es: ",ultimo
		print "El penultimo digito del numero evaluado es: ",penultimo
		
	except ValueError:
		print "Error..."
		
if __name__ == '__main__':
	main()
