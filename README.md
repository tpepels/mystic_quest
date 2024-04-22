# Project: Operation Data Resurgence

## Initial Setup: Installing PrettyTable

Before diving into the project, you'll need to install the `prettytable` Python package. This package will help you display your generated game world entities in a well-formatted and easy-to-read table format. To install `prettytable`, run the following command in your terminal:

```bash
pip install prettytable
```

Or, if you're using Python 3, use:

```bash
pip3 install prettytable
```

## Background Story

### The Crisis

In an unprecedented event, VirtuWorld Inc., a leading gaming company, experienced a catastrophic server failure that resulted in a complete loss of all game world data. The incident left the company scrambling as they had neither a backup nor a recovery plan in place—yes, a colossal oversight in today's world of high-availability and redundancy.

VirtuWorld Inc. was facing not only a public relations disaster but also the monumental task of restoring the virtual world and all the entities that make it whole. The loss was immense: characters, items, quests, enemies, events, guilds, and more had vanished, leaving an empty void in place of the once-vibrant realms.

### The Call to Action

Desperate for a solution, VirtuWorld Inc. reached out to your university's computer science department, asking for help to rebuild their world data structure. Given the complexity and sheer volume of data that needed to be restored, they were willing to try anything—even if it meant turning the project into an academic exercise for students. They saw promise in your coding talents and your creative capabilities, enough so that they believe you can rebuild what was lost.

## Objective

Your task is to script the resurgence of the entire game world from scratch. The provided script will generate the properties of all the essential entities like players, guilds, items, enemies, and many more. You can use a predefined JSON schema (`entities.json`) to help populate the world with various entities, using either predefined data sources or your own custom data pools.

### Requirements

- At least the following entity types should be defined: `player`, `event`, `item`, `enemy`, `team`, `npc`, `guild`, and `dialogue`.
- You can choose from a set of predefined value sources like `race_names`, `class_names`, `item_types`, etc., to populate fields for these entities, or you can use basic data types: `datetime`, `int`, `string`, and `float`.
- Customization is encouraged! Feel free to add extra entities, attributes, or any creative twist that you think would make the virtual world more interesting.

## Let's bring the VirtuWorld back to life!

The future of VirtuWorld Inc. and the joy of countless gamers is in your hands. Good luck, and may the odds be ever in your favor to restore the game world to its former glory!

---

For any queries, please reach out to (no-one will answer) [contact@virtuworld.inc](mailto:contact@virtuworld.inc).

Happy coding! 🌐🛠️

# The Data Generation Script

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

_Note that you can run the script without changing anything and it will generate data. If you want to have the data match your schema, you can alter `entities.json` to do so._

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

Feel free to run the script multiple times to generate different sets of data. The generated files can be utilized for various testing and simulation purposes.

---

## Part 3. Entities

The `entities.json` is a JSON-formatted configuration file that defines various entities and their fields. You can change this file, but you do not have to.
You can alter the definition by changing the `entities.json` file. You can use this file to map your schema to a number of entities that are generated by the script. However, there's no way to generate data in such a way that it perfectly matches your shema, so do the best you can, but know that you will have to struggle with the data to load it.
Moreover, you can use `value_sources` to populate your database with pre-generated values

Let's break down the elements:

### Structure

#### `entities`

- **Array**: This holds a collection of entities, each described by a JSON object.

#### Entity Object

- **`name`**: The name of the entity (e.g., "Dialogue", "GuildName", "Character").
- **`type`**: The type of the entity, which categorizes the entity into a specific domain ("player", "event", "item", "enemy", "team", "npc", "guild", "team", "dialogue"). Add this field to tell the script the purpose of a given entity.
- **`fields`**: An array of field objects that describe the attributes of each entity.

#### Field Object

- **`name`**: The name of the field (e.g., "id", "content", "choice_options").
- **`datatype`**: The type of data that the field can hold ("int", "string", "float", "datetime").
- **`type`**: Optional. Defines special types of fields like "primary_key".
- **`value_source`**: Optional. Specifies from where the values for the field should be derived.

### Minimum Requirements

Based on the structure of the file, the minimum that must be defined for an entity is:

- `name`: A string indicating the name of the entity.
- `type`: A string indicating the type of the entity.
- The following types _must_ be defined in your `entities.json`: "player", "event", "item", "enemy", "team", "npc", "guild", "team", "dialogue". This maps your table names to the script's internal entity types such that the generated data makes sense.
- `fields`: An array with at least one field object, which must have:
  - `name`: The name of the field.
  - `datatype`: The datatype of the field.

Here's an example with the minimum fields:

```json
{
  "entities": [
    {
      "name": "user",
      "type": "player",
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

Entity types map your table names to internal definitions used in event generation. For instance, the script needs to know how npc's and dialogue are stored in your database so that it can generate npc's that initiate dialogue.

You _must_ at least define these entity types:

- `player`
- `event`
- `item`
- `enemy`
- `team`
- `npc`
- `guild`
- `dialogue`

You may assign any type _more than once_. For instance: if you store NPC's in three different tables, then you can mark three entities as type `npc`. The script will then generate unique id's for all records over the three tables. Moreover, the script will treat the `enemy` type as the `npc` type by generating non-overlapping id's for both entity types. That means that if you treat `enemy` as `npc` in your schema, the script will still generate importable data for both the `npc` and `enemy` types.
These are the foundational elements of the game world and its logic. The script will generate events based on these types. Map these entity types to the tables that store them in your database.

Let say that in your database the data related to the human players is stored in the table characters:
`characters`
| Column | Type |
|-------------|--------|
| ID PK | int |
| first_name | str |
| class | str |
| strength | int |
| intelligence| int |
| dexterity | int |
| level | int |
| last_login | datetime |

Then you can create an entity for your table as follows:

```json
{
  "name": "character",
  "type": "player",
  "fields": [
    {
      "name": "id",
      "datatype": "int",
      "type": "primary_key"
    },
    {
      "name": "first_name",
      "datatype": "string",
      "value_source": "first_names"
    },
    {
      "name": "class",
      "datatype": "string",
      "value_source": "class_names"
    },
    {
      "name": "strength",
      "datatype": "int"
    },
    {
      "name": "intelligence",
      "datatype": "int"
    },
    {
      "name": "dexterity",
      "datatype": "int"
    },
    {
      "name": "level",
      "datatype": "int"
    },
    {
      "name": "last_login",
      "datatype": "datetime"
    }
  ]
}
```

Note the use of type `player` here, used to tell the script that this table holds player information in your game.

#### Value Source

The `value_source` can be any of the predefined categories ("blueprints", "enemy_names", "guild_names", etc.). These sources serve as the pool from which values for fields will be derived. So if you want the script to generate some meaningful values for a given table, use these to generate the following types of data:

## Value Source Descriptions

| Key                  | Description                                                             |
| -------------------- | ----------------------------------------------------------------------- |
| `blueprints`         | Source for generating random blueprint data for in-game entities.       |
| `blueprint_types`    | Source for randomly selecting the types of blueprints available.        |
| `enemy_names`        | Source for generating random names for enemy characters.                |
| `enemy_types`        | Source for randomly classifying enemies into various categories.        |
| `guild_names`        | Source for generating random names for different guilds.                |
| `guild_types`        | Source for describing random types of guilds (e.g., trading, warrior).  |
| `team_names`         | Source for generating random team names for in-game squads.             |
| `dialogues`          | Source for generating random dialogue lines for in-game conversations.  |
| `event_names`        | Source for generating random names for in-game events.                  |
| `first_names`        | Source for generating random first names for characters.                |
| `last_names`         | Source for generating random last names for characters.                 |
| `item_names`         | Source for generating random names for in-game items.                   |
| `race_names`         | Source for randomly listing names of character races.                   |
| `race_descriptions`  | Source for randomly listing descriptions of character races.            |
| `item_types`         | Source for categorizing random item types (e.g., swords, potions).      |
| `class_names`        | Source for defining random classes available for characters.            |
| `class_descriptions` | Source for providing brief descriptions of each randomly defined class. |
| `kingdom_names`      | Source for generating random names for various kingdoms.                |
| `npc_types`          | Source for specifying random types of Non-Playable Characters (NPCs).   |
| `npc_descriptions`   | Source for describing the roles of each randomly specified type of NPC. |

You do not have to use these, not specifying a value_source in your json will generate random data for the given type.

### How Students Can Customize

1. **Modify Fields**: You can decide what fields are important for each entity type, from primary identifiers to descriptors and attributes.

2. **Value Sources**: You can choose to use predefined value sources or create their own categories. They can also decide not to use a value source for specific fields, like IDs or counters.

3. **Data Types**: You can specify the data type for each field according to their need, choosing from "int", "string", "datetime" or "float".

4. **Optional Types**: You must specify one primary key for each entity, the best option is to set it to name: "id" with datatype "int".

5. **New Entity Types**: While they should at least include the essential entity types, they are free to create new ones as needed by their project.

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

In this example, the "player" entity has been customized to include a "username" field and an "inventory" field, along with other standard attributes like "id" and "race". Note that, the "name" "Player" is the name for the table in your database (i.e. you may change this and it will not have any effect on the functioning of the script), whereas the "type" player is the type that informs the script that it is the table where player information is stored.
