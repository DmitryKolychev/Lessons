team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 2153.31451
team2_time = 18015.2
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'
tasks_total = 82
time_for_task = ((team1_time+team2_time)/(score_1+score_2))
print('Использование %:')
print("В команде Мастера кода участников: %s! " % (team1_num))
print("Итого сегодня в командах участников: %s и %s!" % (team1_num, team2_num))

print('\nИспользование format():')

print("Команда Волшебники данных решила задач: {}!".format(score_2))
print("Волшебники данных решили задачи за {}с!".format(team2_time))

print('\nИспользование f-строк:')
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_for_task:.2f} секунды на задачу!') # округляю до сотых
