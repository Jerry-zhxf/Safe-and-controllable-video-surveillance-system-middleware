# -*- coding:utf-8 -*-
# Author : Zhxf
# Data : 2019/5/12 10:13
from time import sleep
import time

def func():
    sleep(10)
    now_time = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
    return now_time

if __name__ == "__main__":
    str = func()
    print(str)