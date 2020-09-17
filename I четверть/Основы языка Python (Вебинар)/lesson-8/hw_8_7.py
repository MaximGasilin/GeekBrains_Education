# Задание #7
#
# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив
# сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.


class ComplexNumbers:

    def __init__(self, real, image):
        self.real = real
        self.image = image

    def __str__(self):
        return f'({self.real}, {self.image} i)'

    @staticmethod
    def __convert_other__(other):
        # Проверка того, что "партнером" нашему классу в операции будет число (int, float), комплексное или сам класс
        if isinstance(other, ComplexNumbers):
            other_real = other.real
            other_image = other.image
        elif isinstance(other, complex):
            other_real = other.real
            other_image = other.imag
        elif isinstance(other, float) or isinstance(other, int):
            other_real = other
            other_image = 0
        else:
            raise ValueError('Операция возможно только между комплексными числами, числами и классом ComplexNumbers!')

        return other_real, other_image

    @staticmethod
    def __custom_add__(r1, i1, r2, i2):
        # выполняет сложение по правилам комплексных чисел
        return ComplexNumbers(r1 + r2, i1 + i2)

    @staticmethod
    def __custom_mul__(r1, i1, r2, i2):
        # выполняет умножение по правилам комплексных чисел
        return ComplexNumbers(r1 * r2 - i1 * i2, r1 * i2 + i1 * r2)

    @staticmethod
    def __custom_div__(r1, i1, r2, i2):
        # выполняет деление по правилам комплексных чисел
        real = (r1 * r2 + i1 * i2) / (r2 * r2 + i2 * i2)
        image = (i1 * r2 - r1 * i2) / (r2 * r2 + i2 * i2)
        return ComplexNumbers(real, image)

    def __add__(self, other):
        other_real, other_image = self.__convert_other__(other)
        return self.__custom_add__(self.real, self.image, other_real, other_image)

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        other_real, other_image = self.__convert_other__(other)
        return self.__custom_mul__(self.real, self.image, other_real, other_image)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __sub__(self, other):
        return self.__add__(-1 * other)

    def __rsub__(self, other):
        other_real, other_image = self.__convert_other__(other)
        return self.__custom_add__(other_real, other_image, -1 * self.real, -1 * self.image)

    def __truediv__(self, other):
        other_real, other_image = self.__convert_other__(other)
        return self.__custom_div__(self.real, self.image, other_real, other_image)

    def __rtruediv__(self, other):
        other_real, other_image = self.__convert_other__(other)
        return self.__custom_div__(other_real, other_image, self.real, self.image)


if __name__ == '__main__':
    im_1 = ComplexNumbers(5, 4)
    im_2 = ComplexNumbers(3, 2)

    s_1 = 5 + 4j
    s_2 = 3 + 2j

    print(f'{im_1} * {im_2} =')
    print(f'    мой класс      : {im_1 * im_2}')
    print(f'    Python complex : {s_1 * s_2}')
    print()

    print(f'{23} * {im_2} =')
    print(f'    мой класс      : {23 * im_2}')
    print(f'    Python complex : {23 * s_2}')
    print()

    print(f'{im_1} * {11} =')
    print(f'    мой класс      : {im_1 * 11}')
    print(f'    Python complex : {s_1 * 11}')
    print()

    print(f'{im_1} + {im_2} =')
    print(f'    мой класс      : {im_1 + im_2}')
    print(f'    Python complex : {s_1 + s_2}')
    print()

    print(f'{im_1} + {5} =')
    print(f'    мой класс      : {im_1 + 5}')
    print(f'    Python complex : {s_1 + 5}')
    print()

    print(f'{9.345} + {im_2} =')
    print(f'    мой класс      : {9.345 + im_2}')
    print(f'    Python complex : {9.345 + s_2}')
    print()

    print(f'{im_1} - {im_2} =')
    print(f'    мой класс      : {im_1 - im_2}')
    print(f'    Python complex : {s_1 - s_2}')
    print()

    print(f'{im_1} - {9} =')
    print(f'    мой класс      : {im_1 - 9}')
    print(f'    Python complex : {s_1 - 9}')
    print()

    print(f'{70.345} - {im_2} =')
    print(f'    мой класс      : {70.345 - im_2}')
    print(f'    Python complex : {70.345 - s_2}')
    print()

    print(f'{im_1} / {im_2} =')
    print(f'    мой класс      : {im_1 / im_2}')
    print(f'    Python complex : {s_1 / s_2}')
    print()

    print(f'{s_1} / {im_2} =')
    print(f'    мой класс      : {s_1 / im_2}')
    print(f'    Python complex : {s_1 / s_2}')
    print()

    print(f'{im_1} / {s_2} =')
    print(f'    мой класс      : {im_1 / s_2}')
    print(f'    Python complex : {s_1 / s_2}')
    print()

    print(f'{im_1} / {-2} =')
    print(f'    мой класс      : {im_1 / -2}')
    print(f'    Python complex : {s_1 / -2}')
    print()

    print(f'{100} / {im_2} =')
    print(f'    мой класс      : {100 / im_2}')
    print(f'    Python complex : {100 / s_2}')
    print()
