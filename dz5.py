plus = int(input('введите выручку вашей фирмы в этом месяце'))
minus = int(input('Введите издержки вашей фирмы за этот месяц'))
profit = int(plus - minus)
rent = int(profit / minus)
if profit > 0:
    print(f'Поздравляем! Ваш бизнес в прибыли! Рентабельность прибыли составляет {rent:.2f} %')
    work_people = int(input('Сколько работников трудятся в вашей фирме?'))
    cash = int(profit / work_people)
    print(f'В расчете на одного сотрудника прибыль фирмы составляет {cash:.2f}')
if profit == 0:
    print('Пока Ваш бизнес выходит в 0, но это хороший старт!')
if profit < 0:
    print('К сожалению, Ваш бизнес в минусе! Приложите больше усилий!')
