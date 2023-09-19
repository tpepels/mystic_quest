import json
import random
from faker import Faker

fake = Faker()
min_id = 101
max_id = 300
actions = ["CREATE", "DELETE", "UPDATE"]

def generate_log(entity, action):
    log = {
        "entity": entity,
        "action": action
    }
    return log

def generate_player_data(num_records=100):
    player_data = []
    ids = random.sample(range(min_id, min_id + num_records + max_id), num_records)
    for id_ in ids:
        player = {
            "id": id_,
            "name": fake.name(),
            "email": fake.email(),
            "level": random.randint(1, 100),
            "guild": fake.company_suffix() if random.choice([True, False]) else None,
            "action": random.choice(actions)
        }
        player_data.append(generate_log(player, player['action']))
    return player_data

def generate_quest_data(num_records=100):
    quest_data = []
    ids = random.sample(range(min_id, min_id + num_records + max_id), num_records)
    for id_ in ids:
        quest = {
            "id": id_,
            "title": fake.catch_phrase(),
            "description": fake.text(),
            "reward": random.randint(100, 1000),
            "status": random.choice(["Incomplete", "Complete", "In Progress", None]),
            "action": random.choice(actions)
        }
        quest_data.append(generate_log(quest, quest['action']))
    return quest_data

def generate_item_data(num_records=100):
    item_data = []
    ids = random.sample(range(min_id, min_id + num_records + max_id), num_records)
    for id_ in ids:
        item = {
            "id": id_,
            "name": fake.color_name(),
            "type": random.choice(["Weapon", "Armor", "Potion"]),
            "price": round(random.uniform(1, 100), 2),
            "in_stock": random.randint(0, 100),
            "action": random.choice(actions)
        }
        item_data.append(generate_log(item, item['action']))
    return item_data

def generate_guild_data(num_records=50):
    guild_data = []
    ids = random.sample(range(min_id, min_id + num_records + max_id), num_records)
    for id_ in ids:
        guild = {
            "id": id_,
            "name": fake.company(),
            "realm": fake.city(),
            "membership_count": random.randint(1, 50),
            "action": random.choice(actions)
        }
        guild_data.append(generate_log(guild, guild['action']))
    return guild_data

def generate_player_login_logout(num_records=50):
    records = []
    for _ in range(num_records):
        record = {
            "id": random.randint(min_id, min_id + num_records + max_id),
            "timestamp": fake.date_time_this_month(),
            "action": random.choice(["LOGIN", "LOGOUT"])
        }
        records.append(record)
    return records

def generate_quest_log(num_records=50):
    records = []
    for _ in range(num_records):
        record = {
            "id": random.randint(min_id, min_id + num_records + max_id),
            "timestamp": fake.date_time_this_month(),
            "action": random.choice(["STARTED", "COMPLETED"])
        }
        records.append(record)
    return records

def generate_item_transaction_log(num_records=50):
    records = []
    for _ in range(num_records):
        record = {
            "id": random.randint(min_id, min_id + num_records + max_id),
            "timestamp": fake.date_time_this_month(),
            "action": random.choice(["BOUGHT", "SOLD"])
        }
        records.append(record)
    return records

def generate_class_change_log(num_records=50):
    records = []
    for _ in range(num_records):
        record = {
            "id": random.randint(min_id, min_id + num_records + max_id),
            "timestamp": fake.date_time_this_month(),
            "action": "CLASS_CHANGE",
            "new_class": random.choice(["Warrior", "Mage", "Archer"])
        }
        records.append(record)
    return records

def main():
    n = 200
    player_data = generate_player_data(n)
    quest_data = generate_quest_data(n)
    item_data = generate_item_data(n)
    guild_data = generate_guild_data(n/2)
    player_login_logout = generate_player_login_logout(n)
    quest_logs = generate_quest_log(n*2)
    item_logs = generate_item_transaction_log(n*3)
    class_change_logs = generate_class_change_log(n/2)

    all_data = {
        "player_login_logout": player_login_logout,
        "quest_logs": quest_logs,
        "item_logs": item_logs,
        "class_change_logs": class_change_logs,
        "player_logs": player_data,
        "quest_logs": quest_data,
        "item_logs": item_data,
        "guild_logs": guild_data
    }

    with open("messy_gaming_data.json", "w") as f:
        json.dump(all_data, f, indent=4)

if __name__ == "__main__":
    main()
