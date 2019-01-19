print('\n4. Определить, какое число в массиве встречается чаще всего.\n')

a = [1, 2, 3, 1, 2, 2]

often = 0

for i in set(a):
    if a.count(i) > often:
        often = a.count(i)
        most = i
print(f'Чаще всего в массиве {a} встречается число {most}.\n\n')

print('5.В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.\n\n')

a = [1, -3, -3, -2, 3, 1, 0, -3, -4, 6, -1, 5]

max_negative = -1 * float("inf")

for i, el in enumerate(a):
    if 0 > el > max_negative:
        max_negative = el
        position = i

if max_negative == -1 * float("inf"):
    print(f'В массиве {a} нет отрицательных элементов!')
else:
    print(f'В массиве {a}:')
    print(f'{max_negative} - максимальный отрицательный элемент, на {i}-й позиции(позиции нумеруются с 1)')
