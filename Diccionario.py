
user = {
    "name": "Gustavo",
    "age": 30,
    "is_active": True,
    "courses": ["Python", "JavaScript", "Django"],
    'settings': {
        'theme': 'dark',
        'notifications': True
    }
}
print(list(user.keys()))
print(list(user.values()))
print(list(user.items()))
# Modificar valores
user['name'] = 'Pedro'
user['age'] = 34
print(list(user.items()))
# Agregar nuevos pares clave-valor
user.setdefault('id',100)
print(list(user.items()))

# devuelve el valor de la clave especificada si existe, de lo contrario devuelve None
courses = user.get('courses', [])
print(courses)
# Agregar un nuevo curso a la lista de cursos
courses.append('Python')
courses.append('Django')

# Actualizar el diccionario con los nuevos valores
user.update({
    'name': 'Ana',
    'age': 28,
    'courses': courses
})
print(list(user.items()))

# Eliminar pares clave-valor
del user['age']
print(list(user.items()))
valor = user.pop('is_active')
print('Valor eliminado:', valor)
print(list(user.items()))

# Limpiar el diccionario
user.clear()
print(list(user.items()))