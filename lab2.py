import numpy

print('Задание №1\n')
array1 = numpy.random.randint(-3, 3, size=(10, 10))
minor = array1[1:5, 6:10]
print(array1)
print(minor)
print(numpy.linalg.det(minor))
print('Задание №2')
first = numpy.random.uniform(15,37,(3,4))
second = numpy.random.uniform(15,37,(4,2))
print(first)
print(second)
print('результаты')
print('векторный')
vec = numpy.empty((3,2), float)
for i in range(3):
    for j in range(2):
        vec[i, j] = numpy.sum(first[i, :] * second[:, j])
print(vec)
print('матричный')
for i in range(3):
    vec[i, :] = numpy.dot(first[i, :], second)
print(vec)
print('numpy')
print(numpy.dot(first, second))
print('Задание №3')
