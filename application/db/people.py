from datetime import datetime
import time


def get_employees():
    datetime_now = datetime.now()
    print(datetime_now.strftime("%H:%M:%S"), ' - ', end='')
    num = 42
    print(f'Сформирован список работников для расчета заработной платы, всего '
          f'- {num} человека')
    print()
    time.sleep(1)
    return num
