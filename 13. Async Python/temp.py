import time
from threading import Thread


def oiii():
    print("Sleep for 2 sec")
    time.sleep(2)
    print("Wake up after 2 sec")


# for _ in range(5):
#     t = Thread(target=oiii)
#     t.start()
#     t.join()  # iska mtlb same hi hua ki wait karo uss thread ke execute hone ka fir aage badho

threads = []
for _ in range(5):
    t = Thread(target=oiii)
    t.start()
    threads.append(t)


for thread in threads:
    print(thread)
    thread.join()

print("finished")
