numberr = int(input('Введите время в секундах'))
hour = numberr // 3600
min = (numberr // 60) % 60
sec = numberr % 60
if hour < 10:
    hour = (f'0{hour}')
    if min < 10:
        min = (f'0{min}')
        if sec < 10:
            sec = (f'0{sec}')

print(f'{hour} : {min} : {sec}')


