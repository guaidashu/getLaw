import time
from concurrent.futures import ThreadPoolExecutor
from time import sleep

from tool.function import debug


def task(k, s):
    sleep(k)
    debug(s)


if __name__ == "__main__":
    # pool = ThreadPoolExecutor(max_workers=2)
    # info = ['a', 'b', 'c', 'd', 'e', 'f']
    # for k, v in enumerate(info):
    #     pool.submit(task, 1, v)
    if int(time.time() - 0) > 15:
        debug(int(time.time() - 0))



