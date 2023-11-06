from threading import Thread
import time
import random
import queue

counter = 0
job_queue = (
    queue.Queue()
)  # isme queue ka data jayega lekin usme bhi lock lagana parega taaki ek time pe ek hi cheez print ho
counter_queue = (
    queue.Queue()
)  # this queue is for counter variable so that same one thread one time

# These will execute first bcoz samajh gya
counter_queue.put_nowait(10)
job_queue.put_nowait("Bef")


# if queue is open for data then give that data to any thread and wait
def increment_manager():
    global counter
    while True:
        increment = (
            counter_queue.get()
        )  # this waits until an item is available and locks the queue
        time.sleep(random.random())
        old_counter = counter
        time.sleep(random.random())
        counter = old_counter + increment
        time.sleep(random.random())
        job_queue.put((f"New counter value {counter}", "------------"))
        time.sleep(random.random())
        counter_queue.task_done()  # this unlocks the queue


# printer_manager and increment_manager run continuously because of the `daemon` flag.
Thread(target=increment_manager, daemon=True).start()


def printer_manager():
    while True:
        for line in job_queue.get():
            time.sleep(random.random())
            print(line)
        job_queue.task_done()
        # available for next queue


# printer_manager and increment_manager run continuously because of the `daemon` flag.
Thread(target=printer_manager, daemon=True).start()


# to put vaue in queue no need for .get bcoz kaun pehle kare kya farak parta hai
def increment_counter():
    counter_queue.put(1)
    time.sleep(random.random())


print("This Work Right")
worker_threads = [Thread(target=increment_counter) for thread in range(10)]

for thread in worker_threads:
    time.sleep(random.random())
    thread.start()

for thread in worker_threads:
    thread.join()  # wait for it to finish

# Above for in loop is just for putting value in queue
print("Finished Before join")
# dEKH PEHLE counter pe lagaya bcoz counter me already 10 rhega toh jab tak vo kahtm hoga tab tak sab print ho jayege
counter_queue.join()  # wait for counter_queue to be empty
job_queue.join()  # wait for job_queue to be empty
print("Finished After join")
