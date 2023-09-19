# Project README: Operation Data Resurgence

## Background Story

### The Crisis

In an unprecedented event, VirtuWorld Inc., a leading gaming company, experienced a catastrophic server failure that resulted in a complete loss of all game world data. The incident left the company scrambling as they had neither a backup nor a recovery plan in place—yes, a colossal oversight in today's world of high-availability and redundancy.

VirtuWorld Inc. was facing not only a public relations disaster but also the monumental task of restoring the virtual world and all the entities that make it whole. The loss was immense: characters, items, quests, enemies, events, guilds, and more had vanished, leaving an empty void in place of the once-vibrant realms.

### The Call to Action

Desperate for a solution, VirtuWorld Inc. reached out to your university's computer science department, asking for help to rebuild their world data structure. Given the complexity and sheer volume of data that needed to be restored, they were willing to try anything—even if it meant turning the project into an academic exercise for students. They saw promise in your coding talents and your creative capabilities, enough so that they believe you can rebuild what was lost.

## Objective

Your task is to script the resurgence of the entire game world from scratch. Your script will define the properties of all the essential entities like players, guilds, items, enemies, and many more. You can use a predefined JSON schema (`entities.json`) to help populate the world with various entities, using either predefined data sources or your own custom data pools.

### Requirements

- At least the following entity types should be defined: `player`, `event`, `item`, `enemy`, `team`, `npc`, `guild`, and `dialogue`.
- You can choose from a set of predefined value sources like `race_names`, `class_names`, `item_types`, etc., to populate fields for these entities, or you can use basic data types like `int`, `string`, and `float`.

- Customization is encouraged! Feel free to add extra entities, attributes, or any creative twist that you think would make the virtual world more interesting.

## Let's bring the VirtuWorld back to life!

The future of VirtuWorld Inc. and the joy of countless gamers is in your hands. Good luck, and may the odds be ever in your favor to restore the game world to its former glory!

---

For any queries, please reach out to (no-one will answer) [contact@virtuworld.inc](mailto:contact@virtuworld.inc).

Happy coding! 🌐🛠️

# README.md for the Data Generation Script

## Part 1: How to Run the Script

### Introduction

This script is designed to generate synthetic data for a set of entities such as `player`, `event`, `item`, `enemy`, etc. These entities are defined in a JSON file named `entities.json`.

### Usage

To execute the script, run the following command:

```bash
python generate_data.py
```

#### How it Works

1. **Import Modules**: Essential Python libraries like `datetime`, `json`, `random`, and `uuid` are imported at the beginning.
2. **Utility Functions**: Utility functions like `print_colorful_table()`, `get_random_entity()`, and `generate_random_value()` are defined to aid the data generation process.

3. **Entity Definitions**: The `entities.json` file is read to load the entity definitions.

4. **Data Generation**:

   - A loop iterates over each entity definition to generate a random number of records.
   - For each entity, another loop iterates to populate each field with a suitable random value.

5. **Shuffle and Save**: All generated records are then shuffled and saved into two files: `generated_entities.txt` and `generated_events.txt`.

---

## Part 2: Generated Files

### 1. `generated_entities.txt`

This file contains the randomly generated records for various entities such as `player`, `item`, `team`, etc. The records are shuffled and stored in a human-readable JSON-like format.

**Sample:**

```
--- Team ---

"id"=615
"team_name"="SoulHarvesters"
"kingdom"="Cimmeria"
"n_members"=803


--- Enemy ---

"id"=249
"enemy_name"="Dire Bat"
"enemy_type"="Humanoid"
"hitpoints"=137
"warcry"="lkoywegr"


--- Event ---

"id"=905
"event_name"="The Scarlet Eclipse"
"event_time"=143
```

### 2. `generated_events.txt`

This file contains a list of events that describe relationships between various entities. These events are also generated randomly based on predefined rules for entity interactions.

**Sample:**

```
=====
[Event Type]: npc_with_dialogue
[Timestamp]: 2022-02-24T08:19:01
[Entity1]: {'id': 831, 'npc_type': 'Lore_Masters', 'first_name': 'Zaela', 'last_name': 'Stonewall', 'location': 676.84}
[Entity2]: {'id': 390, 'content': "Y'arrr, what be ye doin' in these parts? Ah, treasure hunting, I see. Well, X marks the spot... or was it Y?", 'choice_options': 200}
[Value]: Ended Conversation
=====
[Event Type]: player_with_team
[Timestamp]: 2022-01-06T15:50:08
[Entity1]: {'id': 800, 'first_name': 'Illinor', 'last_name': 'Thundersong', 'race': 'Dwarf', 'class': 'Healer', 'guild': 'Elemental Lords'}
[Entity2]: {'id': 579, 'team_name': 'Star_Wanderers', 'kingdom': 'Valoria', 'n_members': 701}
[Value]: Captained
=====
[Event Type]: player_with_npc
[Timestamp]: 2022-03-08T21:27:21
[Entity1]: {'id': 919, 'first_name': 'Thaelen', 'last_name': 'Iceshard', 'race': 'Dwarf', 'class': 'Archer', 'guild': "Ocean's Children"}
[Entity2]: {'id': 307, 'npc_type': 'Skill_Trainers', 'first_name': 'Zandalar', 'last_name': 'Skullcrusher', 'location': 709.51}
[Value]: Talked
[Additional Entity Type]: dialogue
[Additional Entity]: {'id': 635, 'content': 'It was the best of times, it was the worst of quests.', 'choice_options': 387}
=====
```

**Note**: If there is an additional entity involved in the event, it will be represented under `[Additional Entity Type]` and `[Additional Entity]`.

---

Feel free to run the script multiple times to generate different sets of data. The generated files can be utilized for various testing and simulation purposes.

The `entities.json` file appears to be a JSON-formatted configuration file that defines various entities and their fields for some kind of game or simulation. Let's break down the elements:

### Structure

#### `entities`

- **Array**: This holds a collection of entities, each described by a JSON object.

#### Entity Object

- **`name`**: The name of the entity (e.g., "Dialogue", "GuildName", "Character").
- **`type`**: The type of the entity, which seems to categorize the entity into a specific domain (e.g., "dialogue", "guild", "player").

- **`fields`**: An array of field objects that describe the attributes of each entity.

#### Field Object

- **`name`**: The name of the field (e.g., "id", "content", "choice_options").
- **`datatype`**: The type of data that the field can hold (e.g., "int", "string").
- **`type`**: Optional. Defines special types of fields like "primary_key".
- **`value_source`**: Optional. Specifies from where the values for the field should be derived.

### Minimum Requirements

Based on the structure of the file, the minimum that must be defined for an entity is:

- `name`: A string indicating the name of the entity.
- `type`: A string indicating the type of the entity.
- `fields`: An array with at least one field object, which must have:
  - `name`: The name of the field.
  - `datatype`: The datatype of the field.

Here's an example with the minimum fields:

```json
{
  "entities": [
    {
      "name": "MinimalEntity",
      "type": "someType",
      "fields": [
        {
          "name": "id",
          "datatype": "int"
        }
      ]
    }
  ]
}
```

### Essential Points

#### Entity Types

Students must at least define these entity types:

- `player`
- `event`
- `item`
- `enemy`
- `team`
- `npc`
- `guild`
- `dialogue`

These are the foundational elements of the game world and its logic.

#### Value Source

The `value_source` can be any of the predefined categories ("blueprints", "enemy_names", "guild_names", etc.) or the basic data types ("int", "string", "float"). These sources serve as the pool from which values for fields will be derived.

### How Students Can Customize

1. **Modify Fields**: Students can decide what fields are important for each entity type, from primary identifiers to descriptors and attributes.

2. **Value Sources**: They can choose to use predefined value sources or create their own categories. They can also decide not to use a value source for specific fields, like IDs or counters.

3. **Data Types**: They can specify the data type for each field according to their need, choosing from "int", "string", or "float".

4. **Optional Types**: Students may include additional meta-types or attributes for specific fields, like specifying a primary key.

5. **New Entity Types**: While they should at least include the essential entity types, they are free to create new ones as needed by their project.

6. **Complex Types**: Advanced structures like arrays or nested objects could also be used if the project demands more complexity.

### Example of a Customized Entity

Here's an example of a customized "player" entity:

```json
{
  "name": "Player",
  "type": "player",
  "fields": [
    {
      "name": "id",
      "datatype": "int",
      "type": "primary_key"
    },
    {
      "name": "username",
      "datatype": "string"
    },
    {
      "name": "race",
      "datatype": "string",
      "value_source": "race_names"
    },
    {
      "name": "level",
      "datatype": "int"
    },
    {
      "name": "inventory",
      "datatype": "string",
      "value_source": "item_names"
    }
  ]
}
```

In this example, the "player" entity has been customized to include a "username" field and an "inventory" field, along with other standard attributes like "id" and "race".
