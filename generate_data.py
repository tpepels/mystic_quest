import csv
import datetime
import json
import random

from prettytable import PrettyTable

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
    print()
    
"""
Value source generation
"""    

def load_csv_to_list(file_name, entity_type):
    """
        Load data from a CSV file to a list based on the entity_type.
        
        Parameters:
        file_name (str): The name of the CSV file to read.
        entity_type (str): The type of the entity, used to determine how to read the data.

        Returns:
        tuple: A tuple containing two lists.
            - The first list contains values from the first column of the CSV.
            - The second list contains values from the second column of the CSV, if applicable.

        Exceptions:
        FileNotFoundError: Raised if the file specified by file_name is not found.
        Exception: Catches all other exceptions and prints an error message.

        Example Usage:
        >>> load_csv_to_list('kingdoms.csv', 'kingdom')
        (['Kingdom1', 'Kingdom2'], [])
        
        >>> load_csv_to_list('npcs.csv', 'npc')
        (['NPC1', 'NPC2'], ['Description1', 'Description2'])
    """
    
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
        raise FileNotFoundError()

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

# A dictionary with all value sources
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


# Start and end dates for the generated data
start_date = datetime.datetime(2021, 1, 1, 0, 0, 0)
end_date = datetime.datetime(2023, 9, 14, 23, 59, 59)

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
    elif datatype == 'datetime':
        return generate_random_timestamp(start_date, end_date).isoformat()
    else:
        return None
    
import random

def generate_random_timestamp(start, end):
    """
    Generate a random datetime between `start` and `end`

    Args:
        start (int): The lower bound of the random datetime
        end (int): The upper bound of the random datetime

    Returns:
        (datetime): a datetime object between `start` and `end`
    """
    time_between_dates = end - start
    random_number_of_seconds = random.randrange(int(time_between_dates.total_seconds()))
    return start + datetime.timedelta(seconds=random_number_of_seconds)

def generate_word_like_string(length):
    """
    Generate a word-like string of a specified length with realistic phoneme structures.
    
    Parameters:
    length (int): The length of the word-like string to generate.

    Returns:
    str: A generated word-like string of the specified length.

    Example Usage:
    >>> generate_word_like_string(5)
    'pralo'
    
    >>> generate_word_like_string(8)
    'tramisca'

    Notes:
    - The function uses clusters of consonants and individual vowels to create realistic word-like strings.
    - Phoneme structures are simulated to ensure that clusters of vowels and consonants are reasonable.
    """
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

def generate_relation(entity1_type, entity2_type):
    """
    Generate a relation between two types of game entities.
    
    Parameters:
    entity1_type (str): The type of the first entity involved in the relation.
    entity2_type (str): The type of the second entity involved in the relation.
    
    Returns:
    tuple: A tuple containing:
        - value (str or None): A string representing the relation type or None if no relation is defined.
        - additional_entity_type (str or None): The type of an additional entity involved in the relation, or None.

    Example Usage:
    >>> generate_relation("player", "npc")
    ('Talked', 'dialogue')
    
    >>> generate_relation("npc", "quest")
    ('Gave Quest', None)

    Notes:
    - The function defines predefined relations between various game entity types.
    - The 'additional_entity_type' provides context for more complex relations that involve an additional entity.
    
    """
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
    
# Read the JSON file containing the entity definitions
with open('entities.json', 'r') as f:
    entity_definitions = json.load(f)['entities']

last_used_ids = {}
# Dictionary to store generated records for each entity type
all_generated_records = {}
# Define the entity types
entity_types = ["player", "event", "item", "enemy", "team", "npc", "guild", "team", "dialogue"]
# Collect the types from entity definitions
defined_entity_types = set(entity['type'] for entity in entity_definitions)

# Check for missing entity types and throw an exception if any are missing
missing_entity_types = set(entity_types) - defined_entity_types
if missing_entity_types:
    raise ValueError(f"The following entity types are missing in the entity definitions: {', '.join(missing_entity_types)}. All types must be defined; \n {', '.join(entity_types)}")

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

            # Generate primary key and store with unique integer ID
            if field.get('type') == 'primary_key':
                if entity_type == 'enemy':
                    pk_type = 'npc'
                else:
                    pk_type = entity_type
                # Initialize counter for new entities
                if pk_type not in last_used_ids:
                    last_used_ids[pk_type] = 0
                
                # Increment counter for the entity
                last_used_ids[pk_type] += random.randint(1, 3)
                # Store the primary key
                record[field_name] = last_used_ids[pk_type]

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

for _ in range(20000):
    value = additional_entity_type = None  # Initialize to None
    # Skip this iteration if no valid relationship is found
    while value is None:
        entity1_type = random.choice(entity_types)
        entity2_type = random.choice(entity_types)

        while entity1_type == entity2_type:
            entity2_type = random.choice(entity_types)

        # Generate value based on entity types
        value, additional_entity_type = generate_relation(entity1_type, entity2_type)

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
        
print("-"*40)
print("\n- Data generation complete! - \n")
print("Two files have been generated:\n - 'generated_events.txt' and,\n - 'generated_entities.txt'.\n Load the contents of these files into your database.\n")
print("-"*40)