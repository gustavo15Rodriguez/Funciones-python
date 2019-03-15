#-*-coding:utf-8-*-

'''6. Construir una función que reciba como parámetro un entero y retorne el carácter al cual
pertenece ese entero como código ASCII.'''

def encontrar_codigo(num):
	chr(num)
	num2 = chr(num)
	return num2

def main():
	try:
		num = int(raw_input("Digite el numero deseado: "))
		solucion = encontrar_codigo(num)
		print solucion
		
	except ValueError:
		print "Error..."
if __name__ == '__main__':
	main()
