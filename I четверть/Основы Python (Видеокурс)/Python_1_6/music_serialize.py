# Задание # 1
#
# Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы, например:
# my_favourite_group = {
# ‘name’: ‘Г.М.О.’,
# ‘tracks’: [‘Последний месяц осени’, ‘Шапито’],
# ‘Albums’: [{‘name’: ‘Делать панк-рок’,‘year’: 2016},
# {‘name’: ‘Шапито’,‘year’: 2014}]}
#
# С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал.
# Записать результаты в файлы group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8.

import pickle
import json

my_favourite_group = {
    'name': 'Eisbrecher',
    'tracks': ['Volle Kraft Voraus', '1000 Narben', 'Schock', 'Zwischen Uns', 'Rot Wie Die Liebe',
    'Himmel, Arsch Und Zwirn', 'Schlachtbank', 'Dreizehn', 'Unschuldsengel', 'Nachtfieber', 'Noch zu retten',
    'Fehler machen Leute', 'Der Flieger', 'So oder so',
    'Was ist hier los?', 'Besser', 'Sturmfahrt', 'In einem Boot', 'Automat',
    'Eisbär', 'Der Wahnsinn', 'Herz auf', 'Krieger', 'Das Gesetz', 'Wo geht der Teufel hin',
    'Wir sind "Rock‘n‘Roll"', 'D-Zug', 'Das Leben wartet nicht'],
    'Albums': [{'name': 'Schock', 'year': 2015}, {'name': 'Sturmfahrt', 'year': 2017}]}

my_favourite_group_json = json.dumps(my_favourite_group)
my_favourite_group_byte = pickle.dumps(my_favourite_group)

print(my_favourite_group_json)
print(my_favourite_group_byte)

with open('group.json', 'w', encoding='utf-8') as file_obj:
    json.dump(my_favourite_group_json, file_obj)

with open('group.pickle', 'wb') as file_obj:
    pickle.dump(my_favourite_group_byte, file_obj)

