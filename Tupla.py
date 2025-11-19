setting = ("Hola", 42, 3.14, True)
print(setting)
print(type(setting))
print(setting[0])
print(setting[1])
print(setting[2])
print(setting[3])
print(type(setting))

courses = ('MongoDB', 'Java', 'NextJS', 'C#', 'MySQL', 'PHP' )
var1, var2, var3, var4, var5, var6 = courses
print(var1,var2,var3,var4, var5, var6)

#unpacking con asterisco
course1, course2, *other_courses = courses
print(course1, course2, other_courses)

var1, var2, _, _, var5, var6 = courses
print(var1,var2,var5, var6)

#ZIP
user = ['user1', 'user2', 'user3']
cursos = ('Curso1', 'Curso2', 'Curso3')
score = (85, 90, 95)

user_and_courses = list(zip(user, cursos, score))
print(type(user_and_courses))
print(user_and_courses)

user_scores = tuple(zip(user, cursos, score))
print(type(user_scores))
print(user_scores)

#Funciones integradas para tuplas
numbers = (1, 2, 4, 3, 4, 5, 6, 7, 8, 9, 10)
print('longitud ' + str(len(numbers)))
print('maximo ' + str(max(numbers)))
print('minimo ' + str(min(numbers)))
print('suma ' + str(sum(numbers)))
print('count 4 ' + str(numbers.count(4)))
print(4 in numbers) #True/False
print(numbers.index(5))
