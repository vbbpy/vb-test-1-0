print('Программа сортировки массива методом пузырька')
print()

x = 11
while x > 10:
    print('Введите размер массива от 0 до 10 ')
    x = int(input())

m = []
import random
for i in range(x):
    y = random.randint(1, 100)
    m.append(y)
print('Ваш исходный  массив ', m)

b = m.copy()
b.sort()

for j in range(x-1):
    for k in range(x-1):
        if m[k] > m[k+1]:
            m[k], m[k+1] = m[k+1], m[k]

print('Сортированный массив ', m)

print('Сортировка by b.sort ', b)