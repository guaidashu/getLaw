import threading
from time import sleep

from tool.function import debug


mylock = threading.RLock()
num = 0


# noinspection PyMethodMayBeStatic
class TestThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)
        debug("开始 " + name)

    def run(self):
        global num
        while True:
            mylock.acquire()
            if num > 10:
                mylock.release()
                break
            num = num + 1
            debug(self.name + ": 得到num值为" + str(num))
            mylock.release()

    def setNum(self):
        global num
        num = 0


def a_test():
    threads = list()
    for k in range(3):
        tmpK = k + 1
        threads.append(TestThread("线程" + str(tmpK)))
    for k in range(3):
        threads[k].start()
    for k in range(3):
        threads[k].join()
    threads[0].setNum()
    debug("完毕")


if __name__ == "__main__":

    for i in range(3):
        a_test()


