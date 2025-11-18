# Crear una matriz 3x3
matrix = [
    #0  1  2
    [2, 5, 7],  #0
    [4, 1, 9],  #1
    [6, 3, 8]  #2
]
print(matrix[0])  # Imprime la primera fila: [2, 5, 7]
print(matrix[1][2])  # Imprime el elemento en la segunda fila, tercera columna: 9
print(matrix[2][2])  # Imprime el elemento en la tercera fila, tercera columna: 8

pares = all(element % 2 == 0 for element in matrix[0])
print('Todos los elementos de la primera fila son pares:', pares)
