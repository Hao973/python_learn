# -*- coding: utf-8 -*- 
# @Time : 2019/7/17 上午10:12 
# @Author : FengHao 
# @Site :  
# @File : python_5_39_code.py
# @Software: PyCharm

from time import sleep, time
from threading import Thread, Lock
from collections import deque
from queue import Queue


class MyQueue(object):
    def __init__(self):
        self.items = deque()
        self.lock = Lock()

    def put(self, item):
        with self.lock:
            self.items.append(item)

    def get(self):
        with self.lock:
            return self.items.popleft()


class Worker(Thread):
    def __init__(self, name, func, in_queue, out_queue):
        super().__init__()
        self.name = name
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.polled_count = 0
        self.work_done = 0

    def run(self):
        print('%s run' % self.name)
        while True:
            self.polled_count += 1
            try:
                # print('%s before in_queue.get()' % self.name)
                item = self.in_queue.get()
                # print('%s after in_queue.get()' % self.name)
            except IndexError:
                # print('%s before sleep(0.01)' % self.name)
                sleep(0.01)  # No work to do
                # print('%s after sleep(0.01)' % self.name)
            else:
                # print('%s before func' % self.name)
                result = self.func(item)
                # print('%s After func' % self.name)
                # print('%s before queue.put(result)' % self.name)
                self.out_queue.put(result)
                # print('%s after queue.put(result)' % self.name)
                self.work_done += 1


def download_func(in_value):
    print('download_func')
    return in_value


def resize_func(in_value):
    print('resize_func')
    return in_value


def upload_func(in_value):
    print('upload_func')
    return in_value


def test_func():
    start = time()
    download_queue = MyQueue()
    resize_queue = MyQueue()
    upload_queue = MyQueue()
    done_queue = MyQueue()
    threads = [
        Worker('download', download_func, download_queue, resize_queue),
        Worker('resize', resize_func, resize_queue, upload_queue),
        Worker('upload', upload_func, upload_queue, done_queue)
    ]

    for thread in threads:
        thread.start()
    for _ in range(10):
        download_queue.put(object())

    while len(done_queue.items) < 10:
        #  Do something useful while waiting
        pass

    processed = len(done_queue.items)
    polled = sum(t.polled_count for t in threads)
    print('Processed', processed, 'items after polling', polled, 'times')
    end = time()
    print('Took %.3f seconds ' % (end - start))


queue = Queue()


def consumer():
    print('Consumer waiting')
    queue.get()  # Runs after put() below
    print('Consumer done')


def test_queue_0():
    thread = Thread(target=consumer)
    thread.start()
    print('Producer putting')
    queue.put(object())  # Runs before get() above
    thread.join()
    print('Producer done')


queue1 = Queue(1)  # Buffer size of 1


def consumer_1():
    sleep(0.5)  # Wait
    queue1.get()  # Runs second
    print('Consumer got 1')
    queue1.get()  # Runs fourth
    print('Consumer got 2')


def test_queue_1():
    thread = Thread(target=consumer_1)
    thread.start()
    queue1.put(object())
    print('Producer put 1')
    queue1.put(object())
    print('Producer put 2')
    thread.join()
    print('Producer done')


in_queue = Queue()


def consumer_2():
    print('Consumer waiting')
    work = in_queue.get()  # Done second
    print('Consumer working')
    # Doing work
    # ...
    print('Consumer done')
    in_queue.task_done()  # Done third


def test_queue_2():
    Thread(target=consumer_2).start()
    in_queue.put(object())  # Done first
    print('Producer waiting')
    in_queue.join()  # Done fourth
    print('Producer done')


class ClosableQueue(Queue):
    SENTINEL = object()

    def close(self):
        self.put(self.SENTINEL)

    def __iter__(self):
        while True:
            item = self.get()
            try:
                if item is self.SENTINEL:
                    return  # Case the thread to exit
                yield item
            finally:
                self.task_done()


class StoppableWorker(Thread):
    def __init__(self, name, func, in_queue, out_queue):
        super().__init__()
        self.name = name
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue

    def run(self):
        for item in self.in_queue:
            result = self.func(item)
            self.out_queue.put(result)


def test_close_able_queue():
    start = time()
    download_queue = ClosableQueue()
    resize_queue = ClosableQueue()
    upload_queue = ClosableQueue()
    done_queue = ClosableQueue()
    threads = [
        StoppableWorker('download', download_func, download_queue, resize_queue),
        StoppableWorker('resize', resize_func, resize_queue, upload_queue),
        StoppableWorker('upload', upload_func, upload_queue, done_queue)
    ]

    for thread in threads:
        thread.start()
    for _ in range(10):
        download_queue.put(object())

    download_queue.close()
    download_queue.join()
    resize_queue.close()
    resize_queue.join()
    upload_queue.close()
    resize_queue.join()
    print(download_queue.qsize(), 'items finished')
    end = time()
    print('Took %.3f seconds ' % (end - start))


if __name__ == '__main__':
    print('main start')
    # test_func()
    # test_queue_0()
    # test_queue_1()
    # test_queue_2()
    test_close_able_queue()
    print('main end')
