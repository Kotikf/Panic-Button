from threading import Thread
from datetime import datetime
from datetime import date
import time
import keyboard
import os 


t = 0
flag = 0


def power_off():
    with open('ATTENTION!!!.txt', 'a', encoding='utf-8') as file:
        file.write(f'Попытка входа в систему {date.today()}  {datetime.now().strftime("%H:%M:%S")}\n')
    return os.system('shutdown /s /t 0')


def check_state(delay: int, cur_time=datetime.datetime.now()) -> None:
    new_time = cur_time + datetime.timedelta(seconds=delay)

    while datetime.datetime.now() < new_time:
        if keyboard.is_pressed('ctrl + alt + d'):
            break
    else:
        power_off()

check_state(10)
