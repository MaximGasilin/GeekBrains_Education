# Задание # 1
#
# Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.
# Примечание: Списки фруктов создайте вручную в начале файла.

list_1 = ['Апельсин', 'Ананас', 'Манго', 'Маракуйя', 'Фейхуа', 'Банан', 'Помело', 'Апельсин']
list_2 = ['Апельсин', 'Яблоко', 'Груша', 'Грейпфрут', 'Гранат', 'Хурма', 'Манго', 'Апельсин']

list_common = [el for el in list_1 if list_2.count(el) > 0]
print(list_common)

list_common = [el for el in list_1 if el in list_2]
print(list_common)
