#-*-coding:utf-8-*-

'''7. Construir una función que reciba como parámetro un caracter y retorne el código ASCII asociado a el.'''

def encontrar_codigo(letra):
	ord(letra)
	letras = ord(letra)
	return letras
	
def main():
	try:
		letra = str(raw_input("Digite la letra deseada: "))
		solucion = encontrar_codigo(letra)
		print solucion
		
	except ValueError:
		print "Error..."
if __name__ == '__main__':
	main()
