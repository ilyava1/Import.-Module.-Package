from main import *
from application.salary import *
from application.db.people import *


start_counting()
num = get_employees()
calculate_salary(num)
