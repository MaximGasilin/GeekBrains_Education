from random import randint, choice as random_choice
from faker import Faker

LIST_OF_ORG_FORMS = ('ООО', 'ПАО')


def ex7_gen(filename, size=10, av_summ=95000):

    Faker.seed(0)
    fake = Faker()
    with open(filename, 'w', encoding='utf-8') as f:
        for i in range(0, size):
            print(
                f'{fake.company()} {random_choice(LIST_OF_ORG_FORMS)} '
                f'{randint(av_summ * 0.95, av_summ * 1.05)} '
                f'{randint(av_summ * 0.7, av_summ * 1.3)}',
                file=f)


if __name__ == '__main__':

    file_name = 'lesson_5_task_7_list_of_companies.txt'
    ex7_gen(file_name)
