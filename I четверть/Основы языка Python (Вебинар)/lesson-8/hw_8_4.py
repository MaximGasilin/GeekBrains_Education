# Задание # 4
#

# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
# общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

from abc import ABC, abstractmethod
from inspect import isabstract
import datetime


class OfficeEquipment(ABC):
    # Абстрактный класс для офисной техники.

    inventory_number = 0
    equipment_name = ''

    def __init__(self, equipment_name):
        self.equipment_name = equipment_name
        self.inventory_number = 0

    @abstractmethod
    def set_characteristics(self, **kwargs):
        # Каждый подкласс должен заполнять характеристики конкретного устройства
        pass

    @abstractmethod
    def get_characteristics(self):
        # Каждый подкласс должен описывать собственные характристики: размер, напряжение сети, требование интернета, ...
        pass


class OfEqPrinter(OfficeEquipment):

    model = ''
    manufacturer = ''

    the_principle_of_image_formation = ''
    compatible_cartridges = []

    next_service_date = datetime.date(3000, 1, 1)

    def __init__(self, equipment_name):
        OfficeEquipment.__init__(self, equipment_name)

    def set_characteristics(self, **kwargs):
        for key, value in kwargs.items():
            self.__setattr__(key, value)

    def get_characteristics(self):
        return {"Name": self.equipment_name,
                "Inventory": self.inventory_number,
                "Model": self.model,
                "Manufacturer": self.manufacturer,
                "The Principle Of Image Formation": self.the_principle_of_image_formation,
                "Compatible Cartridges": self.compatible_cartridges,
                "Next Service Date": (None, self.next_service_date)[self.next_service_date < datetime.date(3000, 1, 1)]
                }


class OfEqScanner(OfficeEquipment):

    model = ''
    manufacturer = ''

    next_service_date = datetime.date(3000, 1, 1)

    def __init__(self, equipment_name):
        OfficeEquipment.__init__(self, equipment_name)

    def set_characteristics(self, **kwargs):
        for key, value in kwargs.items():
            self.__setattr__(key, value)

    def get_characteristics(self):
        return {"Name": self.equipment_name,
                "Inventory": self.inventory_number,
                "Model": self.model,
                "Manufacturer": self.manufacturer,
                "Next Service Date": (None, self.next_service_date)[self.next_service_date < datetime.date(3000, 1, 1)]
                }


class OfEqMFU(OfficeEquipment):

    model = ''
    manufacturer = ''

    the_principle_of_image_formation = ''
    compatible_cartridges = []

    rj_45 = False

    next_service_date = datetime.date(3000, 1, 1)

    def __init__(self, equipment_name):
        OfficeEquipment.__init__(self, equipment_name)

    def set_characteristics(self, **kwargs):
        for key, value in kwargs.items():
            self.__setattr__(key, value)

    def get_characteristics(self):
        return {"Name": self.equipment_name,
                "Inventory": self.inventory_number,
                "Model": self.model,
                "Manufacturer": self.manufacturer,
                "The Principle Of Image Formation": self.the_principle_of_image_formation,
                "Compatible Cartridges": self.compatible_cartridges,
                "Сетевой режим" : ('Нет','Есть')[self.rj_45],
                "Next Service Date": (None, self.next_service_date)[self.next_service_date < datetime.date(3000, 1, 1)]
                }


if __name__ == '__main__':

    Pr_1 = OfEqPrinter('Printer Hewlett-Packard')
    Pr_1.set_characteristics(manufacturer='HP',
                             model='107r',
                             the_principle_of_image_formation='Laser',
                             next_service_date=datetime.date(2021, 5, 1))
    compatible_cartridges = ['HP W1105A', 'HP W1106A', 'HP W1107A']
    Pr_1.set_characteristics(compatible_cartridges=compatible_cartridges)
    print(Pr_1.get_characteristics())

    Pr_2 = OfEqPrinter('Printer Brother')
    Pr_2.set_characteristics(manufacturer='Brother',
                             model='HL-L5100DNX',
                             the_principle_of_image_formation='Laser',
                             next_service_date=datetime.date(2021, 4, 1))
    compatible_cartridges = ['Brother TN-3430', 'Brother TN-3480']
    Pr_2.set_characteristics(compatible_cartridges=compatible_cartridges)
    print(Pr_2.get_characteristics())

    Sc_1 = OfEqScanner('Scanner CANON')
    Sc_1.set_characteristics(manufacturer='CANON',
                             model='DR-F120',
                             next_service_date=datetime.date(2022, 10, 1))
    print(Sc_1.get_characteristics())

    Sc_2 = OfEqScanner('Scanner PANASONIC KV-S1015C')
    Sc_2.set_characteristics(manufacturer='PANASONIC',
                             model='KV-S1015C',
                             next_service_date=datetime.date(2021, 4, 1))
    print(Sc_2.get_characteristics())

    MFU_1 = OfEqMFU('MFU KYOCERA ECOSYS M2040DN')
    MFU_1.set_characteristics(manufacturer='KYOCERA',
                              model='ECOSYS M2040DN',
                              the_principle_of_image_formation='Laser',
                              rj_45=True,
                              next_service_date=datetime.date(2021, 1, 1))
    compatible_cartridges = ['TK-1170']
    MFU_1.set_characteristics(compatible_cartridges=compatible_cartridges)
    print(MFU_1.get_characteristics())

    MFU_2 = OfEqMFU('MFU EPSON L4160')
    MFU_2.set_characteristics(manufacturer='EPSON',
                              model='L4160',
                              the_principle_of_image_formation='InkJet',
                              rj_45=False,
                              next_service_date=datetime.date(2020, 10, 1))
    compatible_cartridges = ['C13T03V14A', 'C13T03V24A', 'C13T03V34A', 'C13T03V44A']
    MFU_2.set_characteristics(compatible_cartridges=compatible_cartridges)
    print(MFU_2.get_characteristics())
