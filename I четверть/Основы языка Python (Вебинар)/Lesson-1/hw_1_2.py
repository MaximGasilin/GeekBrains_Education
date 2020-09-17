'''
# 2
Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и
выведите в формате чч:мм:сс. Используйте форматирование строк.
'''

try:
    entering_int_var = int(input("Введите пожалуйста любое целое число сеунд: "))
except ValueError:
    print('Число введено неверно. Будет заменено на 0.')
    entering_int_var = 0

# первый способ перевода
int_var = entering_int_var

hh = int_var // 3600
if hh < 10 :
    hh = '0' + str(hh)
else :
    hh = str(hh)

int_var = int_var % 3600

mm = int_var // 60
if mm < 10 :
    mm = '0' + str(mm)
else :
    mm = str(mm)

ss = int_var % 60
if ss < 10 :
    ss = '0' + str(ss)
else :
    ss = str(ss)

print(f"Время в формате 'hh:mm:ss' первым способом - {hh}:{mm}:{ss}")

# второй способ перевода
int_var = entering_int_var

hh = str(int_var // 3600).zfill(2)
int_var = int_var % 3600
mm = str(int_var // 60).zfill(2)
ss = str(int_var % 60).zfill(2)

print(f"Время в формате 'hh:mm:ss' вторым способом - {hh}:{mm}:{ss}")
