# Задание # 2
#
# Создать модуль music_deserialize.py.
# В этом модуле открыть файлы group.json и group.pickle, прочитать из них информацию.
# И получить объект: словарь из предыдущего задания.

import pickle
import json


with open('group.json', 'r', encoding='utf-8') as file_obj:
    my_favourite_group_json = json.load(file_obj)
print(my_favourite_group_json)
print(type(my_favourite_group_json))
my_favourite_group = json.loads(my_favourite_group_json)
print(my_favourite_group)
print(type(my_favourite_group))

with open('group.pickle', 'rb') as file_obj:
    my_favourite_group_byte = pickle.load(file_obj)
print(my_favourite_group_byte)
print(type(my_favourite_group_byte))
my_favourite_group = pickle.loads(my_favourite_group_byte)
print(my_favourite_group)
print(type(my_favourite_group))
