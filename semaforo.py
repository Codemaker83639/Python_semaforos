import threading
from time import sleep
semaforo = threading.Semaphore(2)

n=0
class hilo(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id

    def run(self):
        semaforo.acquire()
        sleep(3-self.id)
        d.append(self.id)
        semaforo.release()

d=[];
hilos = [hilo(1),hilo(2),hilo(3)]
for h in hilos:
    h.start()

sleep(4)
semaforo.acquire()
print 
d
semaforo.release()