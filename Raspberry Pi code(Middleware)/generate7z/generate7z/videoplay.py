# -*- coding:utf-8 -*-
# Author : Zhxf
# Data : 2019/5/10 10:13

from picamera import PiCamera
from time import sleep
import thread
import datetime as dt
import threading
from jpype import *
import os.path

def convert_to_mp4(source_path,target_path):
    cmod='MP4Box -add '+source_path+' -new '+target_path;
    execute_state = os.system('MP4Box -add '+source_path+' -new '+target_path);
    print(cmod)
    print(execute_state)
    if execute_state==0:
        return True
    else:
        return False

# class MyThread(threading.Thread):
#     def __init__(self, filestr):
#         threading.Thread.__init__(self)
#         self.filestr = filestr

#     def run(self):
#         startJVM("/home/geek/Android/jdk1.6.0_43/jre/lib/i386/server/libjvm.so", "-ea",
#                  "-Djava.class.path=%s" % (jarpath + 'XXX.jar'))
#         JDClass = JClass("jpype.JpypeDemo")
#         jd = JDClass()
#         jprint = java.lang.System.out.println
#         jprint(jd.encryption(self.filestr))

camera = PiCamera()
while 1:
    now_time = dt.datetime.now().strftime('%F-%T')
    now_time = now_time.replace(":","-")
    # print "开始录制"
    camera.resolution = (1920, 1080)
    #camera.start_preview()
    filename = now_time+'.h264'
    camera.start_recording(filename)
    sleep(10)
    camera.stop_recording()
    # print "结束录制"
    print now_time
    #camera.stop_preview()
    #t = MyThread(filename)
    #thread.start_new_thread(convert_to_mp4, (now_time+'.h264', now_time+'.mp4', ))

