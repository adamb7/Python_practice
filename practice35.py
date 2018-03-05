import json
from collections import Counter


def read_json():
    with open("info.json", "r") as read_file:
        info = json.load(read_file)
    return info


def write_json(info):
    with open("info.json", "w") as write_file:
        json.dump(info,write_file)


def count_months(dict_data):
    value_list = dict_data.values()
    new_value_list = []
    for i in value_list:
        new_value_list.append(i[0:2])
    c = Counter(new_value_list)
    month_dict = {}
    for j in sorted(c):
        if j == "01":
            month_dict["January"] = c[j]
        if j == "02":
            month_dict["February"] = c[j]
        if j == "03":
            month_dict["March"] = c[j]
        if j == "04":
            month_dict["April"] = c[j]
        if j == "05":
            month_dict["May"] = c[j]
        if j == "06":
            month_dict["June"] = c[j]
        if j == "07":
            month_dict["July"] = c[j]
        if j == "08":
            month_dict["August"] = c[j]
        if j == "09":
            month_dict["September"] = c[j]
        if j == "10":
            month_dict["October"] = c[j]
        if j == "11":
            month_dict["November"] = c[j]
        if j == "12":
            month_dict["December"] = c[j]
    print(month_dict)


my_dict = {"Albert Einstein": "01/02/2018", "Benjamin Franklin": "02/02/2014", "Ada Lovegood": "01/03/2018"}
write_json(my_dict)
count_months(read_json())
