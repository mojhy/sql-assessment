#made by harrison - animals go brrrr
#imports
import sqlite3

#constants and varible declaration
DATABASE = "animals"

# functions
def get_stuff(query):
    """get stuff"""
    db = sqlite3.connect('animals')
    cursor = db.cursor()
    sql = query
    cursor.execute(sql)
    results = cursor.fetchall()
    for number in results:
        print(f"     {number[0]:<5}{number[1]:<40}{number[2]:<35} {number[4]:<15} {number[3]}")


def add_animals():
    '''adds an animal'''
    get_stuff(f"INSERT INTO ANIMALS ( animal_name, scientific_name, animal_info, could_i_take_it_in_a_fight ) VALUES ({input('animal name')}, {input('scientific name')}, {input('group')}, {input('ranking, 81 to 85, 81 is death')});")

def select_by_ranking():
    '''selects * by the ranking'''
    search = input('what ranking? \n1. im COOKED \n 2. 1 percent chance I dont lose \n 3. ill probably lose \n4. I definitely have a chance \n5. Im whooping their ASS \n')
    

def select_all():
    '''selects all readible data'''
    get_stuff('SELECT ANIMALS.animal_id, ANIMALS.animal_name, ANIMALS.scientific_name, RANKING.could_i_take_it AS fight_rating, INFO."group" AS animal_group FROM ANIMALS JOIN RANKING ON ANIMALS.could_i_take_it_in_a_fight = RANKING.rank_id JOIN INFO ON ANIMALS.animal_info = INFO.info_id;')
    
run = int(input('what do you want to do? '))
if run == 1:
    add_animals()
elif run == 2:
    select_by_ranking()
elif run  == 3:
    select_all()
else:
    print('no')