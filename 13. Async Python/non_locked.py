from threading import Thread
import time
import random

# so here output is messed up because we didn't put any lock in shared memory so due to this we get that messed up output because some threads have incremented the counter then go to sleep for if some other thread reached line 15 then it will look at the incremented value and then prints 4 as output

counter = 0


def increment_counter():
    global counter
    time.sleep(random.randint(0, 2))
    counter += 1
    time.sleep(random.randint(0, 2))
    print(f"New counter value: {counter}")
    time.sleep(random.randint(0, 2))
    print("-----------")


for x in range(10):
    t = Thread(target=increment_counter)
    # print("Before main sleep")
    time.sleep(random.randint(0, 2))
    # print("After main sleep")
    t.start()
    # t.join()


# The concept of locked shared memory will help to resolve this problem as at one time only one thread can access that shared memory this can be acheived through queue
# queue.get method will lock the queue untill something is present and queue.task_done() will release that queue so that other queue can access it
