from threading import Thread
from datetime import datetime
from datetime import date
import time
import keyboard
import os 


t = 0
flag = 0


def power_off():
    with open('ATTENTION!!!', 'a', encoding='utf-8') as file:
        file.write(f'попытка входы в систему {date.today()} в {datetime.now().strftime("%H:%M:%S")}\n')
    return os.system('shutdown /s /t 0') 

    return print('power_off')
    

def count_time(delay: int = 15):
    t = 0
    while True:
        t += 5
        time.sleep(5)
        if t > 5:
            power_off()



def wait_click():

    keyboard.wait('ctrl + alt + d')
    # while True:

    #     keyboard.add_hotkey("ctrl+alt+j", power_off(), count_time())

    #     if flag == 1:
    #         break

if __name__ == '__main__':
    Thread(target = count_time()).start()
    Thread(target = wait_click()).start()
