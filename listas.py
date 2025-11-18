#listas      0         1        2      3
#          -4        -3       -2      -1
fruits = ['manzana', 'pera', 'uva', 'naranja']
print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[3])

#value = fruits[len(fruits)-1]

#otra forma de acceder al ultimo elemento
value1 = fruits[-1]
value2 = fruits[-2]

print(value1)
print(value2)

#Slicing     0            1           2      3       4        5
courses = ['python', 'javascript', 'html', 'css', 'django', 'flask']
print(courses)
new_list = courses[0:3]
print('New_Lista1:', new_list)
new_list2 = courses[:2]
print('New_Lista2:', new_list2)
new_list3 = courses[2:5]
print('New_Lista3:', new_list3)
new_list4 = courses[3:]
print('New_Lista4:', new_list4)
#copiar una lista con slicing
new_list5 = courses[:]
print('New_Lista5:', new_list5)
#salto de elementos en el slicing
new_list6 = courses[::2]
print('New_Lista6:', new_list6)
new_list7 = courses[1::2]
print('New_Lista7:', new_list7)
#invertir una lista con slicing
new_list8 = courses[::-1]
print('New_Lista8:', new_list8)

#agregar elementos a una lista
courses.append('python')
courses.append('typescript')
print('Courses after append:', courses)

#insertar elementos en una posicion especifica
courses.insert(0,"sql_server")
courses.insert(3,"csharp")
print('Courses after insert:', courses)

#Extender una lista con otra lista
new_courses = ['java', 'c++', 'ruby']
courses.extend(new_courses)
print('Courses after extend:', courses)

#Buscar un elemento en una lista
print("ruby" in courses)
print("python" in courses)

print(courses.index('django'))

#Remover elementos de una lista
courses.remove('django')
courses.remove('csharp')
print('Courses after remove:', courses)

#Eliminar el ultimo elemento de una lista
last_course = courses.pop()
print('Popped course:', last_course)

courses.pop(0)
courses.pop(2)
print('Courses after pop:', courses)

#Limpiar una lista
courses.clear()
print('Courses after clear:', courses)