import os
import time
import subprocess

class PanicButton:
    def check_active(self, name, timer=30):
        for i in range(timer):
            if name in subprocess.check_output('tasklist', shell=True).decode('latin-1'):
                break
            time.sleep(1)
        else: 
            return self.power_off(self)


    def power_off(self):
        os.system('shutdown /s /t 0')
