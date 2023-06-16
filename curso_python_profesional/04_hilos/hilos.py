import threading
import time 


class Hilo(threading.Thread):
    def run(self):
        print(f"inicio : {self.name}") # if you use getName() is deprecated
        time.sleep(2)
        print(f"termino : {self.name}")


if __name__ == '__main__':
    for i in range(4):
        hilo = Hilo(name=f"hilo demo {i+1}")
        hilo.start()
        time.sleep(.1)
        