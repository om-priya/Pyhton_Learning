from threading import Thread
import time
from concurrent.futures import ThreadPoolExecutor


def ask():
    start = time.time()
    name = input("Enter your name: ")
    greet = f"Hello {name}"
    print(greet)
    print(f"ask func took {time.time() - start}")


def run_long():
    start = time.time()
    for _ in range(200000000):
        continue
    print(f"run_long took {time.time() - start}")


start = time.time()
ask()
run_long()
print(f"whole function(single threaded) is {time.time() - start}")


thread1 = Thread(target=ask)
thread2 = Thread(target=run_long)

start = time.time()
thread1.start()
thread2.start()

#thread1.join()
thread2.join()
print(f"whole function with threads is {time.time() - start}")

#start = time.time()
#with ThreadPoolExecutor(max_workers=2) as pool:
#    pool.submit(ask)
#    pool.submit(run_long)
#print(f"With thread pool executor {time.time() - start}")
