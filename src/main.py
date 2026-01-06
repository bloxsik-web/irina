from functions.dir import instance
from functions.TimeUtil import get_time
from functions.manager import create_folder, delete_folder, file_add
from functions.MathUtil import CallMath

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
        elif wtf.lower() == "сколько время":
            get_time()
        elif wtf.lower() == "реши пример":
            CallMath()
        elif wtf.lower() == "реши задачу":
            CallMath()
        elif wtf.lower() == "посчитай":
            CallMath()

if __name__ == "__main__":
    main()