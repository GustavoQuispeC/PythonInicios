mensaje = 'Hola mundo!'
print(mensaje)
print('?' in mensaje)
print(len(mensaje))
print(mensaje.index('!'))
print(mensaje[10])

#Aplicando slicing
mensaje2 = mensaje[1:]
print(mensaje2)
print('h' + mensaje2)

print(mensaje.count('o'))
print(mensaje.upper())
print(mensaje.lower())

## Join y split
courses = 'python, javascript, html, css, django, flask'
print(courses)
courses_list = courses.split(', ')
print(courses_list)

courses_string = ' - '.join(courses_list)
print(courses_string)
print(type(courses_string))

print(' '.join(courses))
print(' '.join(courses_list))

# +
first_name = 'Codigo'
last_name = 'Facilito'
full_name = first_name + ' ' + last_name
print(full_name)
# f-string
full_name2 = f'{first_name} {last_name}'
print(full_name2)
#join
full_name3 = ' '.join([first_name,last_name])
print(full_name3)
# %S
full_name4 = 'El nombre es: %s %s' % (first_name, last_name)
print(full_name4)

# Formateo con .format()
nombre = 'Gustavo'
apellido = 'Quispe'
base = 'El mensaje es: Hola {nombre} {apellido}'
print(base.format(nombre = nombre, apellido = apellido))

#Busqueda dentro de la cadena
#in
mensaje = 'Hola mundo, bienvenidos al mundo de Python'
print('Hola' in mensaje)

#count
print(mensaje.count('mundo'))
