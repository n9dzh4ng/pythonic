#!/usr/bin/env python

import threading
from time import sleep, ctime


def loop0():
    print('start loop 0 at:', ctime())
    sleep(4)
    print('loop 0 done at:', ctime())


def loop1():
    print('start loop 1 at:', ctime())
    sleep(8)
    print('loop 1 done at:', ctime())


class ThreadingTest(threading.Thread, loop0()):
    def run(self):
        for message in loop0():
            print(threading.currentThread().getName())


def main():
    print('starting at:', ctime())
    a = ThreadingTest(name="message send")
    b = ThreadingTest(name="message receive")
    b.start()
    a.start()
    print('all DONE at:', ctime())


if __name__ == '__main__':
    main()
