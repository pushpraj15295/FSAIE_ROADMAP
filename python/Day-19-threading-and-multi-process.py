# threading and multi-process

import threading

# example 1: threading
# threading is a way to run multiple threads in a single process
import time

def print_numbers():
    for i in range(10):
        print(i)
        time.sleep(1)

def print_letters():
    for i in range(10):
        print(i)
        time.sleep(1)

# create threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# start threads
# t1.start()
# t2.start()

# join threads
# t1.join() # wait for thread to finish
# t2.join() # wait for thread to finish

print("Threads finished")



# example 2: threading with arguments -------------------------------------------------------------

balance = 200;

def withdraw(amount,time):
    global balance
    
    for i in range(time):
        balance -= amount
        print(f"Withdrew {amount} from balance. New balance is {balance}")
        
def deposit(amount,time):
    global balance
    for i in range(time):
        balance += amount
        print(f"Deposited {amount} into balance. New balance is {balance}")
       
# create threads
t1 = threading.Thread(target=withdraw, args=(100,20)) 
t2 = threading.Thread(target=deposit, args=(100,30))

# start threads
t1.start()
t2.start()

# join threads
t1.join()
t2.join()

print("Threads finished 0----")   