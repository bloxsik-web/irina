import os

def create_folder():
    folder_name = input("Введите название папки: ")
    try:
        os.mkdir(folder_name)
        print("Папка создана")
    except FileExistsError:
        print(f"Папка '{folder_name}' уже существует")
    except Exception as e:
        print(f"Ошибка при создании папки: {e}")

def delete_folder():
    fold_del = input("Введите название папки: ")
    try:
        os.remove(fold_del)
        print("Папка удалена")
    except FileExistsError:
        print(f"Ошибка")
    except Exception as e:
        print(f"Ошибка")

def file_add():
    name_file = input("Введите название файла: ")
    try:
        with open(name_file, 'x') as f:
            pass
        print(f"Файл '{name_file}' успешно создан")
    except FileExistsError:
        print(f"Ошибка: Файл '{name_file}' уже существует")
    except Exception as e:
        print(f"Ошибка: {e}")