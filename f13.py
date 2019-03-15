#-*-coding:utf-8-*-

'''13. Construir una función que reciba como parámetro un entero y un dígito y retorne la
cantidad de veces que se encuentra dicho dígito en dicho entero.'''

def encontrar_digito(num, dig):
	cont=0
	
	while num>0:
		dig1 = num%10
		if dig1 == dig:
			cont+=1
		num=num//10
	
	if cont!=0:
		return "El digito evaluado se encuentra %d veces en el numero anterior."%cont
		
	else:
		return "El digito no se encuentra dentro del numero leido."

def main():
	try:
		num = int(raw_input("Digite el numero deseado: "))
		dig = int(raw_input("Digite el digito deseado: "))
		digito = encontrar_digito(num, dig)
		print digito
		
	except ValueError:
		print "Error..."

if __name__ == '__main__':
	main()
