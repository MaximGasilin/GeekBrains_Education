from random import choice


def my_choice(list):
    if list:
        return choice(list)


if __name__ == '__main__':
    my_list = list(range(50))
    print(my_list)
    print(my_choice(my_list))
