courses = ['python', 'javascript', 'html', 'css', 'django', 'flask']

# Copiar una lista
copy_courses1 = courses[:]
print('Shallow_copy:', copy_courses1)

copy_courses = courses.copy()
print('Copied Courses:', copy_courses)

#Invertir una lista
Courses_reversed1 = courses[::-1] # shallow copy reversed
print('Reversed Courses 1:', Courses_reversed1)

Courses_reversed = courses.reverse()
print('Reversed Courses:', courses)

#Ordenar una lista
courses.sort()
print('Sorted Courses:', courses)

courses.sort(reverse=True)
print('Sorted Courses Descending:', courses)


