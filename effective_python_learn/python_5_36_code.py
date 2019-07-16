# -*- coding: utf-8 -*- 
# @Time : 2019/7/12 10:49 
# @Author : FengHao 
# @Site :  
# @File : python_5_36_code.py
# @Software: PyCharm Community Edition
import subprocess
import time

def test_subprocess():
    proc = subprocess.Popen(['echo', 'Hello from the child!'], stdout=subprocess.PIPE, shell=True)
    out, err = proc.communicate()
    print(out.decode('utf-8'))

def test_subprocess1():
    proc = subprocess.Popen(['sleep', '0.3'])
    while proc.poll() is None:
        print('Working ...')
        # Some time-consuming work here
        # ...
    print('Exit status', proc.poll())

def run_sleep(period):
    proc = subprocess.Popen(['sleep', str(period)])
    return proc

def test_subprocess2():
    start = time.time()
    procs = []
    for _ in range(10):
        proc = run_sleep(0.1)
        procs.append(proc)

    for proc in procs:
        proc.communicate()

    end = time.time()
    print('Finished in %.3f seconds' % (end - start))


if __name__ == '__main__':
    test_subprocess2()
