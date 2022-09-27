from datetime import datetime


def calculate_salary(num):
    datetime_now = datetime.now()
    print(datetime_now.strftime("%H:%M:%S"), ' - ', end='')
    print(f'Сформирована ведомость выплаты заработной платы, всего - {num}'
          f' позиции')
    print()
