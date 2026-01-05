from functions.dir import instance
from functions.manager import create_folder, delete_folder, file_add

def main():
    instance()
    
    while True:
        wtf = input("Введите ваш запрос: ")
        
        if wtf.lower() == "создай папку":
            create_folder()
        elif wtf.lower() == "удали папку":
            delete_folder()
        elif wtf.lower() == "выход":
            break
        elif wtf.lower() == "создай файл":
            file_add()
        
        print()

if __name__ == "__main__":
    main()