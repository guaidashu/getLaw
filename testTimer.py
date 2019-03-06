# coding=utf-8
import signal
import time


def set_timeout(num, callback):
    def wrap(func):
        def handle(signum, frame):
            raise RuntimeError

        def to_do(*args, **kwargs):
            try:
                signal.signal(signal.SIGALRM, handle)
                signal.alarm(num)
                print("start alarm signal")
                r = func(*args, **kwargs)
                print("close alarm signal")
                signal.alarm(0)
                return r
            except RuntimeError as e:
                callback()

        return to_do()

    return wrap


def after_timeout():
    print("超时了")


@set_timeout(2, after_timeout)
def testTimeout():
    time.sleep(3)
    return 'content success'


if __name__ == '__main__':
    print(testTimeout())

