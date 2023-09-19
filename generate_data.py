import csv
import datetime
import json
import random
import uuid

from prettytable import PrettyTable


def load_csv_to_list(file_name, entity_type):
    
    loaded_list = []
    loaded_list_second_column = []
    try:
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
    except FileNotFoundError:
        print(f"File {file_name} not found.")
        return [], []
    except Exception as e:
        print(f"An error occurred: {e}")
        return [], []

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

# Function to print records in a colorful, well-formatted way
def print_colorful_table(entity_name, records):
    """
    Prints records in a colorful, well-formatted way

    Args:
        entity_name (str): The name of the entity to be printed
        records (list): The records to be printed
    """
    if not records:
        return
    # Get headers
    headers = records["records"][0].keys()
    entity_type = records["type"]
    # Create a PrettyTable object
    x = PrettyTable()
    # Set the field names
    x.field_names = headers
    # Populate rows
    for record in records["records"]:
        x.add_row(record.values())

    print(f"{entity_name} ({entity_type=}) Table:")
    print(x)
    print("-"*30)
    print()

def get_random_entity(entity_type):
    """
    Returns a random entity of the given type

    Args:
        entity_type (str): the type of entity to be returned

    Returns:
        str: a random entity of the given type
    """
    if entity_type in all_types:
        return random.choice(all_types[entity_type])
    else:
        return "Unknown entity type"


def generate_random_value(datatype):
    """
    Function to generate random values based on datatype

    Args:
        datatype (str): (int, string, float)

    Returns:
        (int, str, float): a random value for the given datatype
    """
    if datatype == 'int':
        return random.randint(1, 1000)
    elif datatype == 'float':
        return round(random.uniform(1.0, 1000.0), 2)
    elif datatype == 'string':
        return generate_word_like_string(random.randint(3, 8))
    else:
        return None
    
import random


def generate_word_like_string(length):
    vowels = 'aeiou'
    clusters = ['bl', 'br', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl', 'gr', 'pl', 'pr', 'sc', 'sk', 'sl', 'sm', 'sn', 'sp', 'st', 'sw', 'tr']
    # Determine individual consonants that are not part of a cluster
    all_consonants = 'bcdfghjklmnpqrstvwxyz'
    word = ''
    
    n_cons = 0
    n_vowels = 0
    for i in range(length):
        if (n_vowels < 2 and random.randint(0, 2) == 1) or n_cons > 1:
            word += random.choice(vowels)
            n_cons = 0
            n_vowels += 1
        else:
            n_vowels = 0
            if n_cons > 0 or (n_cons == 0 and random.randint(0, 1) == 1):
                word += random.choice(all_consonants)
                n_cons += 1
            else:
                word += random.choice(clusters)
                n_cons += 2
    
    return word

    
# Read the JSON file containing the entity definitions
with open('entities.json', 'r') as f:
    entity_definitions = json.load(f)['entities']

# Dictionary to keep track of generated primary keys and UUIDs
primary_keys = {}
# Dictionary to store generated records for each entity type
all_generated_records = {}
# Define the entity types
entity_types = ["player", "event", "item", "enemy", "team", "npc", "guild", "team", "dialogue"]
# Loop through each entity definition and generate data
for entity in entity_definitions:
    entity_name = entity['name']
    entity_type = entity['type']
    assert entity_type in entity_types, f"Invalid entity type: {entity_type} for entity: {entity_name}..."
    fields = entity['fields']

    # Initialize list to store generated records for this specific entity
    generated_records = []

    for _ in range(random.randint(50, 200)):  # Generate a random number of records for each entity
        record = {}
        for field in fields:
            field_name = field['name']
            datatype = field['datatype']

            # Generate primary key and store with UUID
            if field.get('type') == 'primary_key':
                primary_key = uuid.uuid4()
                primary_keys[(entity_name, primary_key)] = generate_random_value(datatype)
                record[field_name] = primary_keys[(entity_name, primary_key)]

            # Generate value from predefined lists if 'value_source' exists
            elif 'value_source' in field:
                record[field_name] = get_random_entity(field['value_source'])

            # Otherwise, generate a random value based on the datatype
            else:
                record[field_name] = generate_random_value(datatype)

        generated_records.append(record)

    # Add this entity's generated records to the overall dictionary
    all_generated_records[entity_name] = {"type": entity_type, "records": generated_records}

# Print each entity table
for entity_name, value in all_generated_records.items():
    print_colorful_table(entity_name, value)
    print("\n")

# Convert dictionary to list and shuffle it
shuffled_records = [(k, v) for k, records in all_generated_records.items() for v in records["records"]]
random.shuffle(shuffled_records)

# Write shuffled and marked records to a txt file
with open('generated_entities.txt', 'w') as f:
    for entity_type, record in shuffled_records:
        identifier = f"--- {entity_type} ---\n"
        f.write(identifier)
        f.write(json.dumps(record, separators=("", "="), indent=0).replace('{', '').replace('}', ''))
        f.write("\n\n")

# Initialize a list to store generated events
generated_events = []

start_date = datetime.datetime(2021, 1, 1, 0, 0, 0)
end_date = datetime.datetime(2022, 12, 31, 23, 59, 59)

def generate_random_timestamp(start, end):
    time_between_dates = end - start
    random_number_of_seconds = random.randrange(int(time_between_dates.total_seconds()))
    return start + datetime.timedelta(seconds=random_number_of_seconds)

def generate_value(entity1_type, entity2_type):
    value = None
    additional_entity_type = None  # Initialize to None
    
    if entity1_type == "player" and entity2_type == "npc":
        value = random.choice(["Talked", "Fought", "Ignored", "Bought From", "Sold To"])
        if value == "Talked":
            additional_entity_type = "dialogue"
        elif value in ["Bought From", "Sold To"]:
            additional_entity_type = "item"
    elif entity1_type == "npc" and entity2_type == "dialogue":
        value = random.choice(["Started Conversation", "Ended Conversation"])
    elif entity1_type == "npc" and entity2_type == "quest":
        value = random.choice(["Gave Quest", "Completed Quest"])
    elif entity1_type == "item" and entity2_type == "npc":
        value = random.choice(["Given", "Taken"])
    elif entity1_type == "player" and entity2_type == "guild":
        value = random.choice(["Joined", "Left", "Promoted"])
    elif entity1_type == "player" and entity2_type == "team":
        value = random.choice(["Joined", "Left", "Captained"])
    elif entity1_type == "player" and entity2_type == "enemy":
        value = random.choice(["Defeated", "Escaped", "Captured"])
    
    return value, additional_entity_type  # This will return the 'value' and 'additional_entity_type', which may be None



for _ in range(20000):
    value = additional_entity_type = None  # Initialize to None
    # Skip this iteration if no valid relationship is found
    while value is None:
        entity1_type = random.choice(entity_types)
        entity2_type = random.choice(entity_types)

        while entity1_type == entity2_type:
            entity2_type = random.choice(entity_types)

        # Generate value based on entity types
        value, additional_entity_type = generate_value(entity1_type, entity2_type)

    entity1_records = None
    entity2_records = None
    additional_records = None  # For any additional entity types

    for k, v in all_generated_records.items():
        if v["type"] == entity1_type:
            entity1_records = v["records"]
        elif v["type"] == entity2_type:
            entity2_records = v["records"]
        elif additional_entity_type is not None and v["type"] == additional_entity_type:
            additional_records = v["records"]

    if entity1_records and entity2_records:
        entity1_sample = random.choice(entity1_records)
        entity2_sample = random.choice(entity2_records)
        additional_sample = None  # Initialize

        if additional_entity_type and additional_records:
            additional_sample = random.choice(additional_records)

        if additional_sample:
            event = {
                "type": f"{entity1_type}_with_{entity2_type}",
                "timestamp": generate_random_timestamp(start_date, end_date).isoformat(),
                "entity1": entity1_sample,
                "entity2": entity2_sample,
                "value": value,
                "additional_entity_type": additional_entity_type,  # Will be None if not applicable
                "additional_entity": additional_sample  # If not relevant, this will be None
            }
        else:
            event = {
                "type": f"{entity1_type}_with_{entity2_type}",
                "timestamp": generate_random_timestamp(start_date, end_date).isoformat(),
                "entity1": entity1_sample,
                "entity2": entity2_sample,
                "value": value,
            }
        assert not entity1_sample is None, f"entity1_sample is None for entity1_type: {entity1_type}"
        assert not entity2_sample is None, f"entity2_sample is None for entity2_type: {entity2_type}"

        generated_events.append(event)

# Export to a custom text file format
with open('generated_events.txt', 'w') as f:
    for event in generated_events:
        f.write(f"[Event Type]: {event.get('type', 'N/A')}\n")
        f.write(f"[Timestamp]: {event.get('timestamp', 'N/A')}\n")
        f.write(f"[Entity1]: {event.get('entity1', 'N/A')}\n")
        f.write(f"[Entity2]: {event.get('entity2', 'N/A')}\n")
        f.write(f"[Value]: {event.get('value', 'N/A')}\n")
        additional_entity_type = event.get("additional_entity_type", "N/A")
        if additional_entity_type != "N/A":
            f.write(f"[Additional Entity Type]: {additional_entity_type}\n")
            f.write(f"[Additional Entity]: {event.get('additional_entity', 'N/A')}\n")
        f.write("=====\n")