import time

def get_time(): 
    local_time = time.localtime()
    print(f"Сейчас: {time.strftime('%H:%M:%S', local_time)}")