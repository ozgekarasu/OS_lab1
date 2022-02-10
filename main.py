import logging
import threading
import time
import random as rnd 

class Fifo:
    def __init__(self):
        self.first = None
        self.last = None

    def append(self, data):
        node = [data, None] 
        if self.first is None:
            self.first = node
        else:
            self.last[1] = node
        self.last = node

    def pop(self):
        if self.first is None :
            raise IndexError
        node = self.first
        self.first = node[1]
        return node[0]

def ThreadFIFOExecute(Fifo):
    start_single_thread = time.time()
    logging.info("Thread %s: starting")
    time.sleep(2)
    logging.info("Thread %s: finishing")
    random_number=rnd.randint(0,100)
    Fifo.append(random_number)
    end_single_thread = time.time()
    print("Thread takes :",end_single_thread-start_single_thread)

if __name__ == "__main__":
    a = Fifo()
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    threads = list()
    #Time measure for FIFO append() oeprations start here while we are creating the threads in alist to proceed one by one 
    for index in range(100):
        logging.info("Main    : create and start thread %d.", index)
        x = threading.Thread(target=ThreadFIFOExecute, args=(a,))
        threads.append(x)
        x.start()
    start = time.time()

    for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)
    end = time.time()
    print("FIFO TIME :",(end - start))




