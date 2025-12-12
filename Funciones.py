
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

# usando return
def division(numero1, numero2):
    if numero2 == 0:
        return print("Error: No se puede dividir por cero.")
    resultado = numero1 / numero2
    return print(f"El resultado de la division es: {resultado}")

division(11, 0)

#***Devuelve una tupla
def problem():
    return 'Maria', 12, True

dato1, dato2, dato3  = problem()
print(dato1, dato2, dato3)