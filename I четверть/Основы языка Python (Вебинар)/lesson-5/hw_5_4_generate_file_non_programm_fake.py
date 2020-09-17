from random import randint

from num2words import num2words


def ex4_gen(filename, count=20):
    with open(filename, 'w') as f:
        for digit in [randint(1, 100) for i in range(0, count)]:
            # digit = randint(1, 101)
            print(f'{num2words(digit, lang="en")}-{digit}', file=f)
            print(f'{num2words(digit, lang="en")}-{digit}')


if __name__ == '__main__':
    file_name = 'lesson_5_task_4_int_list.txt'
    ex4_gen(file_name)
