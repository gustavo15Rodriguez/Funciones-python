#-*-coding:utf-8-*-

'''50. Construir una función que reciba una matriz 5x5 y retorne la cantidad de veces que se
repite su moda.'''

def llenar_matriz(filas, columnas):
	matriz = []
	for a in range(filas):
		fila = []
		for b in range(columnas):
			num = int(raw_input("Digite el numero deseado: "))
			fila.append(num)
		matriz.append(fila)

	return matriz

def encontrar_total_moda(matriz):
	mayor = 0
	repetidos = []
	for k in range(len(matriz)):
		for l in range(len(matriz[k])):
			cont = 1
			for g in range(len(matriz)):
				for s in range(len(matriz[g])):
					if k != g or l != s:
						if matriz[k][l] == matriz[g][s] != "hola":
							cont+=1
							matriz[g][s] = "hola"
						
			if cont > 1 and cont > mayor:
				mayor = cont
				repetidos.append([matriz[k][l], mayor])
				
			matriz[k][l] = "hola"
			
	if len(repetidos) == 0:
		return 0
		
	else:
		return repetidos				
		
def main():
	try:
		filas = 5
		columnas = 5 
		arreglo = llenar_matriz(filas, columnas)
		moda = encontrar_total_moda(arreglo)
		if moda == 0:
			print "No hay numeros repetidos."
			
		else:
			print "La moda de la matriz anterior es el primer dato, y el segundo dato indica las veces que se retipe dicho dato: "
			
			print moda

	except ValueError:
		print "Error..."

if __name__ == '__main__':
	main()
