# Definir el arreglo
arreglo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Inicializar la variable de suma
suma = 0

# Inicializar las variables de máximo y mínimo
maximo = arreglo[0]
minimo = arreglo[0]

# Iterar sobre el arreglo
for numero in arreglo:
    suma += numero

    # Verificar si el número actual es mayor al máximo
    if numero > maximo:
        maximo = numero

    # Verificar si el número actual es menor al mínimo
    if numero < minimo:
        minimo = numero

# Imprimir el resultado
print("La suma de todos los valores es:", suma)
print("El valor máximo es:", maximo)
print("El valor mínimo es:", minimo)
