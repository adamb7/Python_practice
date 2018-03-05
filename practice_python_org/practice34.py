import json


def create_json(info):
    with open("info.json", "w") as write_file:
        json.dump(info, write_file)


def read_json():
    with open("info.json", "r") as read_file:
        data = json.load(read_file)
    print(data)
    return data


def update_json(key, value):
    data = read_json()
    data[key] = value
    create_json(data)


my_dict = {"Albert Einstein": "03/14/1879", "Benjamin Farnklin": "01/17/1706", "Ada Lovelace": "12/10/1815"}
create_json(my_dict)
new_name = input("Add a new name to db: ")
new_date = input("Add a new date to db: (MM/DD/YYYY) ")
update_json(new_name, new_date)
read_json()
