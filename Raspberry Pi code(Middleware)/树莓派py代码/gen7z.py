# -*- coding:utf-8 -*-
# Author : Zhxf
# Data : 2019/7/27 16:51

import os.path

def gen7z(name, path):
    cmod='7z a -t7z -r '+name+'.7z '+path +'*'
    execute_state = os.system(cmod)
    print(execute_state)
    if execute_state==0:
        return True
    else:
        return False

