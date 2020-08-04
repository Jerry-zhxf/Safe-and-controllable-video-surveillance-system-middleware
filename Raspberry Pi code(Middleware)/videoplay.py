# -*- coding:utf-8 -*-
# Author : Zhxf
# Data : 2019/5/10 10:13

from picamera import PiCamera
from time import sleep
import datetime as dt
import threading
from jpype import *
import os.path

class MyThread(threading.Thread):
    def __init__(self, filestr):
        threading.Thread.__init__(self)
        self.filestr = filestr

    def run(self):
        startJVM("/home/geek/Android/jdk1.6.0_43/jre/lib/i386/server/libjvm.so", "-ea",
                 "-Djava.class.path=%s" % (jarpath + 'XXX.jar'))
        JDClass = JClass("jpype.JpypeDemo")
        jd = JDClass()
        jprint = java.lang.System.out.println
        jprint(jd.encryption(self.filestr))

while 1:
    now_time = dt.datetime.now().strftime('%F-%T')
    camera.resolution = (1920, 1080)
    camera.start_preview()
    filename = '/home/pi/'+now_time+'.h264'
    camera.start_recording(filename)
    sleep(300)
    camera.stop_recording()
    camera.stop_preview()
    t = MyThread(filename)

