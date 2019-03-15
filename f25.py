#-*-coding:utf-8-*-

'''25. Construir una función que reciba como parámetro un entero y un dígito menor o igual a 5
y retorne el dígito del número que se encuentre en la posición especificada por el dígito que
llegó como parámetro.'''

def encontrar_posicion(num, digito):
	if digito >=0 and digito <=5:
		lista = []
		while num>0:
			dig = num%10
			lista.append(dig)
			num = num//10
			
		lista.reverse()
		numero = 0
		for i in range(len(lista)):
			if i ==digito:
				numero = lista[i]
		
				
		if len(lista)<digito+1:
			return "El numero ingresado no tiene la cantidad de digitos a evaluar."

		else:
			return "La posicion exacta del digito a evaluar es: %d"%numero
	
	else:
		return "El digito ingresado no puede ser mayor a 5."
		
def main():
	try:
		num = int(raw_input("Digite el numero deseado: "))
		digito = int(raw_input("Digite un numero entre 0 y 5: "))
		posicion = encontrar_posicion(num, digito)
		print posicion
		
	except ValueError:
		print "Error..."

if __name__ == '__main__':
	main()
