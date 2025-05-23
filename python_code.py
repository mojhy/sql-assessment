#made by harrison - animals go brrrr
#data was taken from reddit btw
#all ratings were made on the assumption that i have a small knife
#imports
import sqlite3
#colour declaraions
r = '\033[31m'
g = '\033[32m'
y = '\033[33m'
b = '\033[34m'
reset = '\033[0m'
br = '\033[41m'
bg = '\033[42m'
by = '\033[43m'
bb = '\033[44m'
bp = '\033[45m'
#constants and varible declaration
DATABASE = "animals"

options = '1. add an animal\n2. select by ranking\n3. select all\n4. search for an animal\n5. kill an animal\n6. edit an animal\n7. advanced\nexit'
db = sqlite3.connect('animals')
cursor = db.cursor()

# functions
def ranking_help(value):
    get_stuff(f'SELECT ANIMALS.animal_id, ANIMALS.animal_name, ANIMALS.scientific_name, RANKING.could_i_take_it AS fight_rating, INFO."group" AS animal_group FROM ANIMALS JOIN RANKING ON ANIMALS.could_i_take_it_in_a_fight = RANKING.rank_id JOIN INFO ON ANIMALS.animal_info = INFO.info_id where could_i_take_it_in_a_fight = {value};')

def get_stuff(query):
    """get stuff"""
    sql = query
    cursor.execute(sql,)
    results = cursor.fetchall()
    for number in results:
        print(f"     {number[0]:<5}{number[1]:<40}{number[2]:<35} {number[4]:<15} {number[3]}")
 
def ranking_nums():
    print(f'{y}from 81 being death, to 85 being easy as hell, {reset}')
    print(f'{y}81, 82, 83, 84, 85,{reset}')
def group_names():
    '''prints group names'''
    print(f'{y}86	Reptile,\n 87	Mammal,\n 88	Insect,\n 89	Arachnid,\n 90	Amphibian,\n 91	Bird,\n 92	Mollusk,\n 93	Cockroach,\n 94	Myriapod{reset}')

def add_animals():
    '''adds an animal'''
    animal_name = input(f'{bb}animal name: {reset}')
    scientific_name = input(f'{bb}scientific name: {reset}')
    group_names()
    group = int(input(f'{bb}group: {reset}'))
    ranking = int(input(f'{bb}ranking, 81 to 85, 81 is death: {reset}'))
    qurey = f"INSERT INTO ANIMALS (animal_name, scientific_name, animal_info, could_i_take_it_in_a_fight) VALUES('{animal_name.title()}', '{scientific_name.title()}', '{group}', '{ranking}');"
    cursor.execute(qurey,)

def select_by_ranking():
    '''selects * by the ranking'''
    search = int(input(f'{y}1. im COOKED \n2. 1 percent chance I dont lose \n3. ill probably lose \n4. I definitely have a chance \n5. Im whooping their ASS \n{bb}what ranking? \n{reset}'))    
    if search == 1:
        ranking_help(81)
    elif search == 2:
        ranking_help(82)
    elif search == 3:
        ranking_help(83)
    elif search == 4:
        ranking_help(84)
    elif search == 5:
        ranking_help(85)

def select_all():
    '''selects all readible data'''
    get_stuff('SELECT ANIMALS.animal_id, ANIMALS.animal_name, ANIMALS.scientific_name, RANKING.could_i_take_it AS fight_rating, INFO."group" AS animal_group FROM ANIMALS JOIN RANKING ON ANIMALS.could_i_take_it_in_a_fight = RANKING.rank_id JOIN INFO ON ANIMALS.animal_info = INFO.info_id;')

def search_animal():
    '''search for a specific animal'''
    animal = input(f'{bb}what animal would you like to search for? {reset}').title()
    get_stuff(f"select * from ANIMALS where animal_name = '{animal}';")

def kill_an_animal():
    animal = input(f'{bb}what animal would you like to kill? {reset}').title()
    query = f'Delete from animals where animal_name = {animal.title()};'
    cursor.execute(query, )

def edit_an_animal():
    print(f'{br}DO NOT CHANGE ANIMAL idS!!!!!!!!!!!!!!!{reset}')
    change = input(f'{bb}what animal do you want to change? {reset}')
    print(f'{y}columms are; \nanimal_name\nscientific_name\ncould_i_take_it_in_a_fight\nanimal_info(group){reset}')
    columm = input(f'{bb}what columm do you want to edit? {reset}')
    if columm == 'could_i_take_it_in_a_fight':
        ranking_nums()
    if columm == 'group':
        group_names()
    changes = input(f"{bb}what do you want to change it to? {reset}")
    query = f"UPDATE animals SET {columm} = '{changes}' WHERE animal_name = '{change}';"
    cursor.execute(query,)

def advanced_():
    cursor.execute(input(f'{bb}Write your own query: {reset}'))
    results = cursor.fetchall()
    for number in results:
        print(f"     {number}")

# main code

print(options)
run = input('what do you want to do? (enter a number) ')
while run.isnumeric() or not run.isnumeric():
    
    if   run == '1':
        add_animals()
    elif run == '2':
        select_by_ranking()
    elif run == '3':
        select_all()
    elif run.lower() == 'exit':
        break
    elif run == '4':
        search_animal()
    elif run == '5':
        kill_an_animal()
    elif run == '6':
        edit_an_animal()
    elif run == '7':
        advanced_()
    else:
        print(f'{r}no{reset}')
    
    print(options)
    run = input('what do you want to do? ')