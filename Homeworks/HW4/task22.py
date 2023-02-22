# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
#Пример:
#11 6
#2 4 6 8 10 12 10 8 6 4 2
#3 6 9 12 15 18

#6 12

n = int(input("Введите кол-во элементов первого набора чисел: "))
m = int(input("Введите кол-во элементов второго набора чисел: "))

list_1 = list()
for i in range(n):
    input_n = int(input("Введите элементы первого набора: "))
    list_1.append(input_n)

list_2 = list()
for i in range(m):
    input_m = int(input("Введите элементы второго набора: "))
    list_2.append(input_m)
    
print(list_1)
print(list_2)

numbers = set(list_1)
numbers2 = set(list_2)
numbers3 = numbers.intersection(numbers2)
sorted_numbers = sorted(numbers3)
print(sorted_numbers)
