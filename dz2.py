number = int(input('Введите время в секундах'))
hour = number // 3600
min = (number // 60) % 60
sec = number % 60
if hour < 10:
    hour = (f'0{hour}')
    if min < 10:
        min = (f'0{min}')
        if sec < 10:
            sec = (f'0{sec}')

print(f'{hour} : {min} : {sec}')


