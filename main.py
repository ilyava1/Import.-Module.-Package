from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime


def start_counting():
    print()
    print(f'{datetime.now().date()}. Программа расчета заработной платы'
          f' запущена.')
    print()
    num = get_employees()
    calculate_salary(num)
    print('Работа программы завершена')


if __name__ == '__main__':
    start_counting()
