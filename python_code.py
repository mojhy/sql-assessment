#made by harrison - animals go brrrr
#data was taken from reddit btw
#all raings were made on the assumption that i have a small knife
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
    get_stuff(f"INSERT INTO ANIMALS ( animal_name, scientific_name, animal_info, could_i_take_it_in_a_fight ) VALUES ({input('animal name: ')}, {input('scientific name: ')}, {input('group: ')}, {input('ranking, 81 to 85, 81 is death')});")

def select_by_ranking():
    '''selects * by the ranking'''
    search = int(input('what ranking? \n1. im COOKED \n2. 1 percent chance I dont lose \n3. ill probably lose \n4. I definitely have a chance \n5. Im whooping their ASS \n'))    
    if search == 1:
        get_stuff('SELECT ANIMALS.animal_id, ANIMALS.animal_name, ANIMALS.scientific_name, RANKING.could_i_take_it AS fight_rating, INFO."group" AS animal_group FROM ANIMALS JOIN RANKING ON ANIMALS.could_i_take_it_in_a_fight = RANKING.rank_id JOIN INFO ON ANIMALS.animal_info = INFO.info_id where could_i_take_it_in_a_fight = 81;')
    elif search == 2:
        get_stuff('SELECT ANIMALS.animal_id, ANIMALS.animal_name, ANIMALS.scientific_name, RANKING.could_i_take_it AS fight_rating, INFO."group" AS animal_group FROM ANIMALS JOIN RANKING ON ANIMALS.could_i_take_it_in_a_fight = RANKING.rank_id JOIN INFO ON ANIMALS.animal_info = INFO.info_id where could_i_take_it_in_a_fight = 82;')
    elif search == 3:
        get_stuff('SELECT ANIMALS.animal_id, ANIMALS.animal_name, ANIMALS.scientific_name, RANKING.could_i_take_it AS fight_rating, INFO."group" AS animal_group FROM ANIMALS JOIN RANKING ON ANIMALS.could_i_take_it_in_a_fight = RANKING.rank_id JOIN INFO ON ANIMALS.animal_info = INFO.info_id where could_i_take_it_in_a_fight = 83;')
    elif search == 4:
        get_stuff('SELECT ANIMALS.animal_id, ANIMALS.animal_name, ANIMALS.scientific_name, RANKING.could_i_take_it AS fight_rating, INFO."group" AS animal_group FROM ANIMALS JOIN RANKING ON ANIMALS.could_i_take_it_in_a_fight = RANKING.rank_id JOIN INFO ON ANIMALS.animal_info = INFO.info_id where could_i_take_it_in_a_fight = 84;')
    elif search == 5:
        get_stuff('SELECT ANIMALS.animal_id, ANIMALS.animal_name, ANIMALS.scientific_name, RANKING.could_i_take_it AS fight_rating, INFO."group" AS animal_group FROM ANIMALS JOIN RANKING ON ANIMALS.could_i_take_it_in_a_fight = RANKING.rank_id JOIN INFO ON ANIMALS.animal_info = INFO.info_id where could_i_take_it_in_a_fight = 85;')

def select_all():
    '''selects all readible data'''
    get_stuff('SELECT ANIMALS.animal_id, ANIMALS.animal_name, ANIMALS.scientific_name, RANKING.could_i_take_it AS fight_rating, INFO."group" AS animal_group FROM ANIMALS JOIN RANKING ON ANIMALS.could_i_take_it_in_a_fight = RANKING.rank_id JOIN INFO ON ANIMALS.animal_info = INFO.info_id;')

# main code
run = input('what do you want to do? ')
while run.isnumeric() or not run.isnumeric():
    
    if run == '1':
        add_animals()
    elif run == '2':
        select_by_ranking()
    elif run  == '3':
        select_all()
    elif run == 'exit':
        break
    else:
        print('no')
    run = input('what do you want to do? ')