#Найдите сумму цифр трехзначного числа.
#Пример:
#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0) |

n = int(input('Введите трехзначное число: '))

if n > 99 and n < 1000:
        a = n // 100
        b = n // 10 % 10
        c = n % 10
        sum = a + b + c
        print(f'Сумма цифр этого числа = {sum}')
else:
        print('Вы ввели не трехзначное число.')