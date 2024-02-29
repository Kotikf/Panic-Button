import os
import time
import subprocess

class PanicButton:
    def check_active(self, name: str, timer: int) -> None:
        for i in range(timer):
            if name in subprocess.check_output('tasklist', shell=True).decode('latin-1'):
                break
            time.sleep(1)
        else: 
            return self.power_off(self)


    def remove_file(self, path):
        with open(path, 'r') as  file:
            text = file.read()
        len_text = len(text)
        zero_fill_line_length = 50
        zero_fill = ['0' * zero_fill_line_length
                      for _
                      in range(len_text // zero_fill_line_length + 1)]
        zero_fill = os.linesep.join(zero_fill)
        with open(path, 'w') as file:
            file.write(zero_fill)


    def power_off(self):
        os.system('shutdown /s /t 0')
