#-*-coding:utf-8-*-

'''23. Construir una función que reciba como parámetro dos enteros y retorne 1 si la diferencia
entre los dos valores es un número primo. Deberá retornar 0 si no es así.'''

def encontrar_diferencia(num1, num2):

	if num1>num2:
		diferencia1 = num1-num2
		cont = 0
		for g in range(1, diferencia1+1):
			if diferencia1%g==0:
				cont+=1
		if cont==2:
			return 1
				
		else:
			return 0
			
	if num2>num1:
		diferencia2 = num2-num1
		cont2 = 0
		for s in range(1, diferencia2+1):
			if diferencia2%s==0:
				cont2+=1
		if cont2==2:
			return 1
					
		else:
			return 0

def main():
	try:
		num1 = int(raw_input("Digite el primer numero: "))
		num2 = int(raw_input("Digite el segundo numero: "))
		primo = encontrar_diferencia(num1, num2)
		print primo
		
	except ValueError:
		print "Error..."

if __name__ == '__main__':
	main()
