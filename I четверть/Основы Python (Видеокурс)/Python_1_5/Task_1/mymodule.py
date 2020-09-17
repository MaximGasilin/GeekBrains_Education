import os


def create_folders():

    my_dir = os.getcwd()
    for i in range(1, 10):
        new_path = os.path.join(my_dir, 'dir_{}'.format(str(i)))
        print(my_dir)
        try:
            os.mkdir(new_path)
        except FileExistsError:
            print(f'Folder {new_path} alredy exist.')

def remove_folders():

    my_dir = os.getcwd()
    for i in range(1, 10):
        new_path = os.path.join(my_dir, 'dir_{}'.format(str(i)))
        print(my_dir)
        try:
            os.rmdir(new_path)
        except FileNotFoundError:
            print(f'Folder {new_path} is not found.')
        except PermissionError:
            print(f'Access to the folder {new_path} is denied.')