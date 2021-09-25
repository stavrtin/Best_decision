'''1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за
четыре квартала для каждого предприятия. Программа должна^
 - определить среднюю прибыль (за год для всех предприятий),
 - отдельно вывести наименования предприятий, чья прибыль выше среднего,
 - отдельно вывести наименования предприятий, чья прибыль ниже среднего.'''


from collections import namedtuple

prop = ['name', 'q1', 'q2', 'q3', 'q4']
Plant = namedtuple('Plant', prop)

plant_dict = []
quantity = int(input('Введите количество предприятий: ===>>  '))

for i in range(quantity):
    name = input('Введите название ' + str(i + 1) + '-го предприятия: ===>>  ')
    profit_q1 = int(input('Введите прибыль 1-го квартала предприятия '+ name + ' : ===>>  '))
    profit_q2 = int(input('Введите прибыль 2-го квартала предприятия '+ name + ' : ===>>  '))
    profit_q3 = int(input('Введите прибыль 3-го квартала предприятия '+ name + ' : ===>>  '))
    profit_q4 = int(input('Введите прибыль 4-го квартала предприятия '+ name + ' : ===>>  '))
    plant_dict.append(Plant(name, profit_q1, profit_q2, profit_q3, profit_q4))

total_profit = 0
for i in plant_dict:
    total_profit += (i.q1 + i.q2 + i.q3 + i.q4)
print('-*-' * 20)
print(f'Общая прибыль:  {total_profit}')
print(f'Средняя прибыль (за год для всех предприятий):  {round(total_profit/quantity,2)}')

low = [i.name for i in plant_dict if (i.q1 + i.q2 + i.q3 + i.q4) < (total_profit/quantity)]
hi = [i.name for i in plant_dict if (i.q1 + i.q2 + i.q3 + i.q4) >= (total_profit/quantity)]
print(f'Список предприятий с доходом менее среднего: {", ".join(low)}')
print(f'Список предприятий с доходом выше среднего: {", ".join(hi)}')

