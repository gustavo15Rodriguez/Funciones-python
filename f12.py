#-*-coding:utf-8-*-

'''12. Construir una función que reciba como parámetro un entero y un dígito y retorne 1 si
dicho dígito está en dicho entero y 0 si no es así.'''

def encontrar_digito(num, dig):
	cont=0
	
	while num>0:
		dig1 = num%10
		if dig1 == dig:
			cont+=1
		num=num//10
	
	if cont!=0:
		return 1
		
	else:
		return 0

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
