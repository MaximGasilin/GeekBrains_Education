# Задание # 6
#
# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров,
# отправленных на склад, нельзя использовать строковый тип данных.

from abc import ABCMeta
import hw_8_4
import datetime


def version_1__str__(self):
    ''' Переопредеелние стандартного вывода, чтобы продемонстрировать возможности метакласса '''
    result = ''
    for dep, equip in self.office_equipment.items():
        result = result + f'{dep}' + '\n'
        for el in equip:
            result = result + f'    {el}' + '\n'
    return result


def version_1_add_department(self, department_name):
    ''' Переопредеелние метода ad_department. Добавив дополнительную проверку,
    но, после проверки, воспроизведя алгоритм старой фукнкции '''
    print(f'Перехват функции ad_department: {department_name}')
    if department_name == '':
        department_name = 'Основной'
    self.old_version_add_department(department_name)


class WarehouseMeta(ABCMeta):
    def __new__(cls, name, bases, namespace):
        namespace['__str__'] = version_1__str__
        ''' Заменил метод __str__ для экземпляров класса'''
        namespace['old_version_add_department'] = namespace['add_department']
        ''' Текущую функцию класса "add_department" скопировал в пространстве имен с новым ключем'''
        namespace['add_department'] = version_1_add_department
        ''' Заменил функцию класса "add_department" новой, улучшенной версией,
            которая проверяет пустоту введенного имени'''

        return super().__new__(cls, name, bases, namespace)


class Warehouse(metaclass=WarehouseMeta):
    def __init__(self, department_name):
        self.default_department_name = department_name
        self.departments = []
        ''' состав департаментов, между которыми можно перемещать технику'''
        self.office_equipment = {}
        ''' состав оргтехники. Словарь, в котором ключ - департамент, значение - список классов OfficeEquipment'''
        self.departments.append(self.default_department_name)
        ''' добавление департамента по-умолчанию'''
        self.office_equipment[department_name] = []
        self.last_inventory_number = 0

    def __get_new_inv_number(self):
        self.last_inventory_number += 1
        return self.last_inventory_number

    def add_department(self, department_name):
        print(f'Вызов основной функции add_department: {department_name}')
        if self.departments.count(department_name) == 0:
            self.departments.append(department_name)
            self.office_equipment[department_name] = []
        else:
            print(f'Департамент {department_name} уже существует. Используйте его. Или введите другое имя.')

    def __find_of_equ(self, off_eq, department_name=''):
        department = None

        if department_name != '':
            if self.office_equipment[department_name].count(off_eq) != 0:
                department = department_name

        if department is None:
            try:
                department = [k for k, el in self.office_equipment.items() if el.count(off_eq) == 1][0]
            except IndexError:
                pass

        return department

    def __remove_of_eq(self, off_eq, department_name=''):
        department = self.__find_of_equ(off_eq, department_name)
        if department is not None:
            self.office_equipment[department].remove(off_eq)
            print(f'{off_eq} перемещен из департамента {department}.')

    def __add_of_equ(self, off_eq, department_name, using_default_dep=False):
        if self.departments.count(department_name) != 0:
            department = department_name
        elif using_default_dep:
            department = self.departments[0]
        else:
            department = None
            print(f'{off_eq} не оприходован ни на {department_name}')

        if department is not None:
            if off_eq.inventory_number == 0:
                off_eq.inventory_number = self.__get_new_inv_number()
            self.office_equipment[department].append(off_eq)
            print(f'{off_eq} помещен в департамент {department}')

    def replace_office_equipment(self, off_eq, department_name, using_default_dep=False):
        if self.departments.count(department_name) == 0:
            print(f'Департамента {department_name} не существует')
            department_name = None
            if using_default_dep:
                department_name = self.departments[0]
                print(f'{off_eq}  помещен в департамент {self.departments[0]} (назаначенный основным))')

        if department_name is not None:
            department = self.__find_of_equ(off_eq)
            if department is not None and department != department_name:
                self.__remove_of_eq(off_eq, department)
            self.__add_of_equ(off_eq, department_name, using_default_dep)
        else:
            print(f'{off_eq} не оприходован ни на одной площадке')


if __name__ == '__main__':

    Pr_1 = hw_8_4.OfEqPrinter('Printer Hewlett-Packard')
    Pr_1.set_characteristics(manufacturer='HP',
                             model='107r',
                             the_principle_of_image_formation='Laser',
                             next_service_date=datetime.date(2021, 5, 1))
    compatible_cartridges = ['HP W1105A', 'HP W1106A', 'HP W1107A']
    Pr_1.set_characteristics(compatible_cartridges=compatible_cartridges)
    # print(Pr_1.get_characteristics())

    Pr_2 = hw_8_4.OfEqPrinter('Printer Brother')
    Pr_2.set_characteristics(manufacturer='Brother',
                             model='HL-L5100DNX',
                             the_principle_of_image_formation='Laser',
                             next_service_date=datetime.date(2021, 4, 1))
    compatible_cartridges = ['Brother TN-3430', 'Brother TN-3480']
    Pr_2.set_characteristics(compatible_cartridges=compatible_cartridges)
    # print(Pr_2.get_characteristics())

    Sc_1 = hw_8_4.OfEqScanner('Scanner CANON')
    Sc_1.set_characteristics(manufacturer='CANON',
                             model='DR-F120',
                             next_service_date=datetime.date(2022, 10, 1))
    # print(Sc_1.get_characteristics())

    Sc_2 = hw_8_4.OfEqScanner('Scanner PANASONIC KV-S1015C')
    Sc_2.set_characteristics(manufacturer='PANASONIC',
                             model='KV-S1015C',
                             next_service_date=datetime.date(2021, 4, 1))
    # print(Sc_2.get_characteristics())

    MFU_1 =hw_8_4.OfEqMFU('MFU KYOCERA ECOSYS M2040DN')
    MFU_1.set_characteristics(manufacturer='KYOCERA',
                              model='ECOSYS M2040DN',
                              the_principle_of_image_formation='Laser',
                              rj_45=True,
                              next_service_date=datetime.date(2021, 1, 1))
    compatible_cartridges = ['TK-1170']
    MFU_1.set_characteristics(compatible_cartridges=compatible_cartridges)
    # print(MFU_1.get_characteristics())

    MFU_2 = hw_8_4.OfEqMFU('MFU EPSON L4160')
    MFU_2.set_characteristics(manufacturer='EPSON',
                              model='L4160',
                              the_principle_of_image_formation='InkJet',
                              rj_45=False,
                              next_service_date=datetime.date(2020, 10, 1))
    compatible_cartridges = ['C13T03V14A', 'C13T03V24A', 'C13T03V34A', 'C13T03V44A']
    MFU_2.set_characteristics(compatible_cartridges=compatible_cartridges)
    # print(MFU_2.get_characteristics())


    Office = Warehouse('Основной')
    Office.add_department('1-й этаж')
    Office.add_department('1-й этаж')
    Office.add_department('2-й этаж')
    Office.add_department('')
    Office.replace_office_equipment(Pr_1, 'Основной')
    Office.replace_office_equipment(Pr_2, 'Основной')
    Office.replace_office_equipment(Sc_1, 'Основной')
    Office.replace_office_equipment(Sc_2, 'Основной')
    Office.replace_office_equipment(MFU_1, 'Основной')
    Office.replace_office_equipment(MFU_2, 'Основной')
    Office.replace_office_equipment(Pr_2, '1-й этаж')
    Office.replace_office_equipment(Sc_1, '1-й этаж')
    Office.replace_office_equipment(MFU_2, '2-й этаж')
    print(Office)
