#-*-coding:utf-8-*-

'''49. Construir una función que reciba una matriz 5x5 y retorne el valor de su moda. La moda
de un conjunto de datos es el dato que mas se repite.'''

def llenar_matriz(filas, columnas):
	matriz = []
	for i in range(filas):
		fila = []
		for j in range(columnas):
			num = int(raw_input("Digite el numero deseado: "))
			fila.append(num)
		matriz.append(fila)
		
	return matriz

def encontrar_moda(matriz):
	mayor = 0
	mayor1 = 0
	repetidos = []
	for k in range(len(matriz)):
		for l in range(len(matriz[k])):
			cont = 1
			cont1 = 1
			for g in range(len(matriz)):
				for s in range(len(matriz[g])):
					if k != g or l != s:
						if matriz[k][l] == matriz[g][s] != "hola":
							cont+=1
							cont1+=1
							matriz[g][s] = "hola"
							
			if cont > 1 and cont > mayor:
				mayor = cont
				mayor1 = matriz[k][l]
				repetidos.append(mayor1)
				
			elif cont > 1 and cont == cont1:
				repetidos.append(matriz[k][l])
				
			matriz[k][l] = "hola"
			
	if len(repetidos)==0:
		return 0
	
	else:
		return repetidos
				
def main():
	try:
		filas = 5
		columnas = 5
		matriz = llenar_matriz(filas, columnas)
		moda = encontrar_moda(matriz)
		if moda == 0:
			print "No hay numeros repetidos."
			
		else:
			print "La moda de la matriz anterior es: ",moda

	except ValueError:
		print "Error..."

if __name__ == '__main__':
	main()
