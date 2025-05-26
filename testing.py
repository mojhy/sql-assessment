import sqlite3
from tabulate import tabulate
DATABASE = "animals"
r = '\033[31m'
g = '\033[32m'
y = '\033[33m'
b = '\033[34m'
reset = '\033[0m'
br = '\033[41m'
bg = '\033[42m'
by = '\033[43m'
bb = '\033[44m'
bo = '\033[46m'

print(f"{y}tots{reset}")
print(f"{r}tots{reset}")
print(f"{b}tots{reset}")
print(f"{g}tots{reset}")
print(f"{br}tots{reset}")
print(f"{bg}tots{reset}")
print(f"{by}tots{reset}")
print(f"{bb}tots{reset}")
print(f"{bo}tots{reset}")

db = sqlite3.connect('animals')
cursor = db.cursor()

query = f'SELECT ANIMALS.animal_id, ANIMALS.animal_name, ANIMALS.scientific_name, RANKING.could_i_take_it AS fight_rating, INFO."group" AS animal_group FROM ANIMALS JOIN RANKING ON ANIMALS.could_i_take_it_in_a_fight = RANKING.rank_id JOIN INFO ON ANIMALS.animal_info = INFO.info_id;'

sql = query
cursor.execute(sql,)
results = cursor.fetchall()
print(tabulate(results))
