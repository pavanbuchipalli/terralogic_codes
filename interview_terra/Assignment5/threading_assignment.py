# import time
# import threading
# num1 =int(input("hhh"))
# num2= int(input("ghghghg"))
# def squres(numbers):
#     # print("squres:")
#     for  i in range(num1+1):
#         time.sleep(0.2)
#         print("squre :-",i*i)
#
# def cubes(numbers):
#     # print("cubes:")
#     for  i in range(num2+1):
#         time.sleep(0.2)
#         print("cubes :-",i*i*i)
#
# t1 =threading.Thread(target=squres,args=(num1,))
# t2 =threading.Thread(target=cubes,args=(num2,))
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
#
from time import sleep
from random import randint
from threading import Thread
from queue import Queue

num1=int(input("select Number of consumer :--"))
num2=int(input("select Number of producer:--"))

def producer(queue):
    print('Producer: Running')
    for i in range(num1):
        value = i+1
        sleep(value)
        item = (i, value)
        queue.put(item)

        print("producer added {}".format(item))
    queue.put(None)
    print('Producer: Done')
def consumer(queue):
    print('Consumer: Running')
    for j in range(num2):
        item = queue.get()
        if item is None:
            break
        sleep(0.2)
        print("consumer got {}".format(item))
    print('Consumer: Done')

queue = Queue()
consumer = Thread(target=consumer, args=(queue,))
consumer.start()
producer = Thread(target=producer, args=(queue,))
producer.start()
producer.join()
consumer.join()