
def count_number (number):
    for n in range(number):
        print(n)
count_number(5)

def multiply(number1, number2):
    result = number1 * number2
    print(f"El resultado de la multiplicación es: {result}")

multiply(4, 5)

def saludo(nombre, apellido, prefijo):
    print(f"Hola, {prefijo} {nombre} {apellido}")

saludo("Juan", "Pérez", "Sr.")