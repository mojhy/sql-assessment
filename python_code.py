# made by Harrison - animals go brrrr
# data was taken from Reddit btw
# all ratings were made on the assumption that I have a small knife

# imports
import sqlite3
from tabulate import tabulate

# colour declarations
r = '\033[31m'  # red
g = '\033[32m'  # green
y = '\033[33m'  # yellow
b = '\033[34m'  # blue
reset = '\033[0m'  # reset to default
br = '\033[41m'  # background red
bg = '\033[42m'  # background green
by = '\033[43m'  # background yellow
bb = '\033[44m'  # background blue
bp = '\033[45m'  # background pink

# constants and variable declarations
DATABASE = "animals"
options = f'{y}1. Add an animal\n2. Select by ranking\n3. Select all\n4. Search for an animal\n5. Delete an animal\n6. Edit an animal\n7. Advanced\nType "exit" to quit{reset}'

db = sqlite3.connect(DATABASE)
cursor = db.cursor()

# functions
def is_exit(input_str):
    """Checks if the user input is 'exit'."""
    return input_str.lower() == "exit"

def get_by_ranking(value):
    """Prints animals by ranking ID."""
    get_query_results(f'''
        SELECT ANIMALS.animal_id, ANIMALS.animal_name, ANIMALS.scientific_name,
        RANKING.could_i_take_it AS fight_rating,
        INFO."group" AS animal_group
        FROM ANIMALS
        JOIN RANKING ON ANIMALS.could_i_take_it_in_a_fight = RANKING.rank_id
        JOIN INFO ON ANIMALS.animal_info = INFO.info_id
        WHERE could_i_take_it_in_a_fight = {value};
    ''')

def get_query_results(query):
    """Runs and prints a SQL query."""
    cursor.execute(query)
    results = cursor.fetchall()
    headers = [description[0] for description in cursor.description]
    print(tabulate(results, headers=headers, tablefmt='github'))

def show_ranking_guide():
    """Prints the ranking guide."""
    print(f'{y}From 81 (certain death) to 85 (easy win):{reset}')
    print(f'{y}81, 82, 83, 84, 85{reset}')

def show_group_names():
    """Prints the animal group IDs and names."""
    print(f'{y}86 Reptile\n87 Mammal\n88 Insect\n89 Arachnid\n90 Amphibian\n91 Bird\n92 Mollusk\n93 Cockroach\n94 Myriapod{reset}')

def add_animal():
    """Adds a new animal to the database."""
    try:
        name = input(f'{bb}Animal name: {reset}')
        if is_exit(name): return

        sci_name = input(f'{bb}Scientific name: {reset}')
        if is_exit(sci_name): return

        show_group_names()
        group = input(f'{bb}Group ID: {reset}')
        if is_exit(group): return

        ranking = input(f'{bb}Fight ranking (81–85): {reset}')
        if is_exit(ranking): return

        query = f"""
            INSERT INTO ANIMALS (animal_name, scientific_name, animal_info, could_i_take_it_in_a_fight)
            VALUES('{name.title()}', '{sci_name.title()}', '{int(group)}', '{int(ranking)}');
        """
        cursor.execute(query)

    except ValueError:
        print('Please enter numbers where required.')
    except sqlite3.Error as e:
        print(f'Database error: {e}')

def select_by_ranking():
    """Selects and prints animals by their ranking."""
    choice = input(f'{y}1. I’m COOKED\n2. 1% chance\n3. Probably lose\n4. I have a chance\n5. I’m winning\n{bb}Choose a rank (1–5): {reset}')
    if is_exit(choice): return

    try:
        mapping = { '1': 81, '2': 82, '3': 83, '4': 84, '5': 85 }
        get_by_ranking(mapping[choice])
    except KeyError:
        print(f'{r}Invalid ranking choice.{reset}')

def select_all():
    """Prints all animals in the database."""
    get_query_results('''
        SELECT ANIMALS.animal_id, ANIMALS.animal_name, ANIMALS.scientific_name,
        RANKING.could_i_take_it AS fight_rating,
        INFO."group" AS animal_group
        FROM ANIMALS
        JOIN RANKING ON ANIMALS.could_i_take_it_in_a_fight = RANKING.rank_id
        JOIN INFO ON ANIMALS.animal_info = INFO.info_id;
    ''')

def search_animal():
    """Searches for a specific animal by name."""
    name = input(f'{bb}Animal to search for: {reset}').title()
    if is_exit(name): return
    get_query_results(f"SELECT * FROM ANIMALS WHERE animal_name = '{name}';")

def delete_animal():
    """Deletes an animal from the database."""
    try:
        name = input(f'{bb}Animal to delete: {reset}').title()
        if is_exit(name): return
        query = f"DELETE FROM ANIMALS WHERE animal_name = '{name}';"
        cursor.execute(query)
    except sqlite3.Error as e:
        print(f'Database error: {e}')

def edit_animal():
    """Edits a selected field of an animal."""
    try:
        print(f'{br}DO NOT CHANGE ANIMAL IDs!!!!!!!!!!!!!!!{reset}')
        name = input(f'{bb}Animal to edit: {reset}')
        if is_exit(name): return

        print(f'{y}Editable fields:\n- animal_name\n- scientific_name\n- could_i_take_it_in_a_fight\n- animal_info (group ID){reset}')
        column = input(f'{bb}Field to edit: {reset}')
        if is_exit(column): return

        if column == 'could_i_take_it_in_a_fight':
            show_ranking_guide()
        elif column == 'animal_info':
            show_group_names()

        new_value = input(f"{bb}New value: {reset}")
        if is_exit(new_value): return

        query = f"UPDATE ANIMALS SET {column} = '{new_value}' WHERE animal_name = '{name}';"
        cursor.execute(query)

    except sqlite3.Error as e:
        print(f'Database error: {e}')

def run_custom_query():
    """Lets the user run a custom SQL query."""
    try:
        custom_query = input(f'{bb}Write your own query: {reset}')
        if is_exit(custom_query): return

        cursor.execute(custom_query)
        results = cursor.fetchall()
        headers = [description[0] for description in cursor.description]
        print(tabulate(results, headers=headers, tablefmt='github'))

    except sqlite3.Error as e:
        print(f'Database error: {e}')

# main program loop
print(options)
action = input(f'{bb}What do you want to do? (enter a number) {reset}')
while True:
    if action == '1':
        add_animal()
    elif action == '2':
        select_by_ranking()
    elif action == '3':
        select_all()
    elif action == '4':
        search_animal()
    elif action == '5':
        delete_animal()
    elif action == '6':
        edit_animal()
    elif action == '7':
        run_custom_query()
    elif action.lower() == 'exit':
        break
    else:
        print(f'{r}That is not a valid option.{reset}')

    print(options)
    action = input(f'{bb}What do you want to do? {reset}')