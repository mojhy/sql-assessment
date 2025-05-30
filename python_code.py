#made by harrison - animals go brrrr
#data was taken from reddit btw
#all ratings were made on the assumption that i have a small knife
#imports
import sqlite3
from tabulate import tabulate
#colour declaraions
r = '\033[31m' # sets colour to red
g = '\033[32m' # sets colour to green
y = '\033[33m' # sets colour to yellow
b = '\033[34m' # sets colour to blue
reset = '\033[0m' # resets the colour to default
br = '\033[41m' # sets background colour to red
bg = '\033[42m' # sets background colour to green
by = '\033[43m' # sets background colour to yellow
bb = '\033[44m' # sets background colour to blue
bp = '\033[45m' # sets background colour to pink
#constants and varible declaration
DATABASE = "animals.db"

password = 'brentonisgae'
options = f'{y}1. add an animal\n2. select by ranking\n3. select all\n4. search for an animal\n5. kill an animal\n6. edit an animal\n7. advanced\nexit{reset}'
db = sqlite3.connect('animals') # connects to my database
cursor = db.cursor() # makes future code more efficient

# functions
def exit_check(check):
    """checks if a input is exit"""
    if check.lower() == "exit":
        print('exited back to main page')
        return True

def ranking_help(value): # this function is only used in 5 instinces, and only exists because sriram and mahi were mad at me
    """helps"""
    get_stuff(f'SELECT ANIMALS.animal_id, ANIMALS.animal_name, ANIMALS.scientific_name, RANKING.could_i_take_it AS fight_rating, INFO."group" AS animal_group FROM ANIMALS JOIN RANKING ON ANIMALS.could_i_take_it_in_a_fight = RANKING.rank_id JOIN INFO ON ANIMALS.animal_info = INFO.info_id where could_i_take_it_in_a_fight = {value};')

def get_stuff(query): # this function runs and prints a query so i dont have to write the same block of code a buch of times
    """get stuff"""
    sql = query
    cursor.execute(sql,)
    results = cursor.fetchall()
    headers = [description[0] for description in cursor.description]
    print(tabulate(results, headers=headers, tablefmt='github'))

def ranking_nums(): # this function just prints some numbers
    """prints some number"""
    print(f'{y}from 81 being death, to 85 being easy as hell, {reset}')
    print(f'{y}81, 82, 83, 84, 85,{reset}')

def group_names(): # this function prints out the group names so i dont have to write it out a bunch of times
    """print the group names"""
    print(f'{y} 86	Reptile,\n 87	Mammal,\n 88	Insect,\n 89	Arachnid,\n 90	Amphibian,\n 91	Bird,\n 92	Mollusk,\n 93	Cockroach,\n 94	Myriapod{reset}')

def add_animals(): # this function lets the user add a animal
    '''adds an animal'''
    try:
        animal_name = input(f'{bb}animal name: {reset}') # animal name
        if exit_check(animal_name): # checks if the varible is an exit thingamiboba
            return
        scientific_name = input(f'{bb}scientific name: {reset}') # takes the scientific name of the animal being added
        if exit_check(scientific_name): # checks if the varible is an exit thingamiboba
            return
        group_names()
        group = input(f'{bb}group: {reset}') # takes the group on the animal being added
        if exit_check(group): # checks if the varible is an exit thingamiboba
            return
        ranking = input(f'{bb}ranking, 81 to 85, 81 is death: {reset}') # takes the ranking of the animal being added
        if exit_check(ranking): # checks if the varible is an exit thingamiboba
            return
        # this is the query that will be executed
        qurey = f"INSERT INTO ANIMALS (animal_name, scientific_name, animal_info, could_i_take_it_in_a_fight) VALUES('{animal_name.title()}', '{scientific_name.title()}', '{int(group)}', '{int(ranking)}');" 
        cursor.execute(qurey,) # this executes the query
        db.commit()
        print(f"{g}animal added successfully{reset}")
    except ValueError:
        print(f'{br}Please enter valid inputs only.{reset}')
    except sqlite3.Error as e:
        print(f'{br}Database error: {e}{reset}')

def select_by_ranking(): # this function will print all animals of 1 ranking
    '''select * by the ranking'''
    search = input(f'{y}1. im COOKED \n2. 1 percent chance I dont lose \n3. ill probably lose \n4. I definitely have a chance \n5. Im whooping their ASS \n{bb}what ranking? \n{reset}')
    if exit_check(search): # checks if the varible is an exit thingamiboba
        return
    # this if statment is here to search for the thing and i know it looks bad but it was WAY worse
    if int(search) == 1:
        ranking_help(81)
    elif int(search) == 2:
        ranking_help(82)
    elif int(search) == 3:
        ranking_help(83)
    elif int(search) == 4:
        ranking_help(84)
    elif int(search) == 5:
        ranking_help(85)

def select_all(): # this function just selects all the readible data in the database in a nice looking way
    '''selects all readible data'''
    get_stuff('SELECT ANIMALS.animal_id, ANIMALS.animal_name, ANIMALS.scientific_name, RANKING.could_i_take_it AS fight_rating, INFO."group" AS animal_group FROM ANIMALS JOIN RANKING ON ANIMALS.could_i_take_it_in_a_fight = RANKING.rank_id JOIN INFO ON ANIMALS.animal_info = INFO.info_id;')

def search_animal(): # this funtion searches for a specific animal by their name
    '''search for a specific animal'''
    animal = input(f'{bb}what animal would you like to search for? {reset}').title()
    if exit_check(animal): # checks if the varible is an exit thingamiboba
        return
    get_stuff(f"select * from ANIMALS where animal_name = '{animal}';")

def kill_an_animal(): # this function deleates an animal from the database
    """kills an animal"""
    user = input("password? ")
    if user == password:
        try:
            animal = input(f'{bb}what animal would you like to kill? {reset}').title() # this inputs the animal that is going to be deleated
            if exit_check(animal): # checks if the varible is an exit thingamiboba
                return
            query = f"Delete from animals where animal_name = '{animal.title()}';"
            cursor.execute(query, )
            print(f"{bg}Animal killed sucessfully{reset}")
        except ValueError:
            print(f'{br}Please enter valid inputs only.{reset}')
        except sqlite3.Error as e:
            print(f'{br}Database error: {e}{reset}')
    else:
        print(f'{br}invalid password{reset}')

def edit_an_animal(): # this function lets the user edit an animal
    """edits an animal"""
    try:
        print(f'{br}DO NOT CHANGE ANIMAL idS!!!!!!!!!!!!!!!{reset}')
        change = input(f'{bb}what animal do you want to change? {reset}') # this inputs the animal that the user wants to change
        if exit_check(change): # checks if the varible is an exit thingamiboba
            return
        print(f'{y}columms are; \nanimal_name\nscientific_name\ncould_i_take_it_in_a_fight\nanimal_info(group){reset}')
        columm = input(f'{bb}what columm do you want to edit? {reset}') # these are the columms
        if exit_check(columm): # checks if the varible is an exit thingamiboba
            return
        if columm == 'could_i_take_it_in_a_fight':
            ranking_nums()
        if columm == 'group':
            group_names()
        changes = input(f"{bb}what do you want to change it to? {reset}")
        if exit_check(changes): # checks if the varible is an exit thingamiboba
            return
        query = f"UPDATE animals SET {columm} = '{changes}' WHERE animal_name = '{change}';"
        cursor.execute(query,)
        db.commit()
        print(f"{g}animal edited successfully{reset}")
    except ValueError:
        print(f'{br}Please enter valid inputs only.{reset}')
    except sqlite3.Error as e:
        print(f'{br}Database error: {e}{reset}')
       

def advanced_(): # i added this because i was bored and the data isnt live anyway so it doesnt matter too much if they deleate the database
    """write ur own query"""
    user = (input(f"{bb}password? {reset}"))
    if user == password:
        try:
            Qss = input(f'{bb}Write your own query: {reset}')
            if exit_check(Qss): # checks if the varible is an exit thingamiboba
                return
            cursor.execute(Qss)
            results = cursor.fetchall()
            headers = [description[0] for description in cursor.description]
            print(tabulate(results, headers=headers, tablefmt='github'))
            db.commit()
            print(f'{g}query ran successfully{reset}')
        except ValueError:
            print(f'{br}Please enter valid inputs only.{reset}')
        except sqlite3.Error as e:
            print(f'{br}Database error: {e}{reset}')
    else:
        print(f"{br}incorrect password{reset}")

# main code

print(options)
run = input(f'{bb}what do you want to do? (enter a number) {reset}')
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
        print(f'{r}that is not an option{reset}')
    
    print(options)
    run = input(f'{bb}what do you want to do? {reset}')
