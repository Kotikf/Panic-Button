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


    def remove_file(self, file_path):
        size = os.path.getsize(file_path)

        with open(file_path, 'wb') as  file:
            file.seek(0)
            file.write(b'\x00' * size)

        os.remove(file_path)


    def power_off(self):
        os.system('shutdown /s /t 0')