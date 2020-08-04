# -*- coding:utf-8 -*-
from gmssl import sm3,func

def signit(value):
    #value为bytes类型
    res = sm3.sm3_hash(func.bytes_to_list(value))
    return res
