day_1 = int(input('сколько километров вы пробежали за первый день?'))
another_day = int(input('Сколько километров вы хотите пробегать в будущем за день?'))
day = 1
while day_1 < another_day:
    day_1 = (day_1 * 1.1)
    day += 1
print(day)











