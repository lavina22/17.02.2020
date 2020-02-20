number = int(input('введите целое положительное число'))
max1 = number % 10
number = number // 10
while number > 0:
    if number % 10 > max1:
        max1 = number % 10
    number = number // 10
print(max1)





