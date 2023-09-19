import random
import csv
import uuid

def load_csv_to_list(file_name, entity_type):
    loaded_list = []
    loaded_list_second_column = []
    
    with open(file_name, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            if entity_type in ['kingdom', 'team_name', 'blueprint', 'dialogue', 'event_name', 'first_name', 'last_name']:
                # Assuming the CSV has a single column for these types
                loaded_list.append(row[0])
            elif entity_type in ['npc', 'enemy', 'item_name', 'guild']:
                # Assuming the CSV has two columns: 'type' and 'description'
                loaded_list.append(row[0])
                loaded_list_second_column.append(row[1])
            else:
                print("Unknown entity type")

    return loaded_list, loaded_list_second_column

blueprints, blueprint_types = load_csv_to_list('data/blueprints.csv', 'blueprint')
enemy_names, enemy_types = load_csv_to_list('data/enemies.csv', 'enemy')
guild_names, guild_types = load_csv_to_list('data/guilds.csv', 'guild')
team_names, _ = load_csv_to_list('data/team_names.csv', 'team_name')
dialogue, _ = load_csv_to_list('data/dialogues.csv', 'dialogue')
event_names, _ = load_csv_to_list('data/event_names.csv', 'event_name')
first_names, _ = load_csv_to_list('data/first_names.csv', 'first_name')
last_names, _ = load_csv_to_list('data/last_names.csv', 'last_name')

item_names, item_types = load_csv_to_list('data/item_names.csv', 'item_name')

# Populate the all_types dictionary
all_types = {
    "blueprints": blueprints,
    "blueprint_types": blueprint_types,
    "enemy_names": enemy_names,
    "enemy_types": enemy_types,
    "guild_names": guild_names,
    "guild_types": guild_types,
    "team_names": team_names,
    "dialogues": dialogue,
    "event_names": event_names,
    "first_names": first_names,
    "last_names": last_names,
    "item_names": item_names,
    "race_names": ['Elf', 'Dwarf', 'Human', 'Orc', 'Undead', 'Naga'],
    "race_descriptions":[
        'Graceful beings connected with nature and magic.',
        'Stout warriors skilled in metallurgy and crafting.',
        'Versatile and adaptive, excelling in various crafts and trades.',
        'Brutal and strong, excelling in physical combat.',
        'Risen from the dead, masters of dark arts and curses.',
        'Serpentine creatures adept in both magic and combat.'
    ],
    "item_types": [
        "Sword", "Staff", "Bow", "Shield",
        "Dagger", "Amulet", "Ring", "Potion",
    ],
    "class_names" :['Warrior', 'Mage', 'Archer', 'Healer', 'Rogue', 'Summoner'],
    "class_descriptions" : [
        'Specializes in tanking damage and close combat.',
        'Offers both damage and support through a variety of spells.',
        'Excels at long-range damage with various types of arrows.',
        'Focuses on healing and buffing teammates.',
        'Skilled in stealth and quick, deadly attacks.',
        'Summons minions to aid in combat.'
    ],
    "kingdom_names" :["Valoria", "Cimmeria", "Elphora", "Orynthia"],
    'npc_types' : ['Quest-givers', 'Shopkeepers', 'Skill_Trainers', 'Lore_Masters'],
    "npc_descriptions" : [
        'Assign tasks and offer rewards',
        'Sell items and resources',
        'Offer skill upgrades for a fee',
        'Provide backstory and clues to hidden secrets'
    ],
}

def generate_unique_ids(data_list):
    id_dict = {}
    for item in data_list:
        unique_id = str(uuid.uuid4())
        id_dict[unique_id] = item
    return id_dict

# Create a new dictionary to hold the ID-mapped data
all_types_with_ids = {}

for key, value in all_types.items():
    all_types_with_ids[key] = generate_unique_ids(value)

def get_random_entity(entity_type):    
    try:
        # Get the correct list based on the entity_type
        entity_list = all_types_with_ids[entity_type]
        # Randomly select a key (unique ID) from the dictionary
        random_key = random.choice(list(entity_list.keys()))
        # Return the corresponding value
        return entity_list[random_key]
    except KeyError:
        return "Unknown entity type"
