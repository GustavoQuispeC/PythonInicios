import sys
print("Usando Python:", sys.version)

# esto es falso para Python: "", 0, 0.0, None, False, [], {}, set(), ()
number1 = 10
number2 = 20
number3 = 30
#if
if number1 < number2 and number1 < number3:
    print(f'El numero {number1} es menor que {number2}')

if number1:
    print('hay un valor en number1')

# if-else
if number1 < number2 or number1 < number3:
    print(f'El numero {number1} es menor  que todos')
else:
    print(f'El numero {number1} no es menor que todos')

#elif
color = 'verde'
if color == 'rojo':
    print('NO puedes pasar')
elif color == 'amarillo':
    print('Debes tener precaucion')
elif color == 'verde':
    print('Puedes pasar')
    #exit()

#match
score = 10
match score:
    case 10:
        print('El score es 10')
    case 20 | 30:
        print('El score es 20 o 30')
    case 40 | 50:
        print('El score es 40 o 50')
    case _:
        print('El score no es 10, 20 o 30')

# operador ternario
value = 4
message = 'es numero par' if value % 2 == 0 else 'es numero impar'
print(f'El valor {value} {message}')

#for
nombres = {
    'nombre':'Gustavo',
    'edad':30,
    'ciudad':'Lima'
}
for clave, valor in nombres.items():
    print(f'{clave} - {valor}')


cosas = ['Mesa', 'Silla', 'Computadora']
for cosa in cosas:
    print(cosa)

#Range
for number in range(10):
    print(number)

for number in range(5,16):
    print(number)
