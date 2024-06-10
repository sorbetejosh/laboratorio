

filas = int(input("Ingrese el número de filas de la matriz: "))
columnas = int(input("Ingrese el número de columnas de la matriz: "))


matriz = []
print("Ingrese los elementos de la matriz:")
for i in range(filas):
    fila = [int(input(f"Elemento [{i+1}, {j+1}]: ")) for j in range(columnas)]
    matriz.append(fila)


suma_total = 0
for fila in matriz:
    suma_total += sum(fila)

maximo = matriz[0][0]
minimo = matriz[0][0]
for fila in matriz:
    for elemento in fila:
        if elemento > maximo:
            maximo = elemento
        if elemento < minimo:
            minimo = elemento


suma_filas = [sum(fila) for fila in matriz]


suma_columnas = [0] * columnas
for fila in matriz:
    for j in range(columnas):
        suma_columnas[j] += fila[j]


print("\nMatriz ingresada:")
for fila in matriz:
    print(fila)

print("\nResultados:")
print(f"Suma de todos los elementos: {suma_total}")
print(f"Elemento máximo: {maximo}")
print(f"Elemento mínimo: {minimo}")
print(f"Suma de cada fila: {suma_filas}")
print(f"Suma de cada columna: {suma_columnas}")

