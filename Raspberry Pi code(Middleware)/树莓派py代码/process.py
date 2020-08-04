# -*- coding:utf-8 -*-

from picamera import PiCamera
from time import sleep
import threading
import time
import datetime as dt
import threading
import os.path
import os
import SM2
import SM3
import SM4
import uuid
import paramiko
import datetime


def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False


def encryptMP4(file, key, path):
    with open(file, 'rb') as v:
        value = v.read()
    v.close()
    with open(key, 'rb') as w:
        sm4key = w.read()
    w.close()
    enc_mp4 = SM4.encrypt(sm4key, value)
    with open(path + 'testmp4.enc', 'wb') as q:
        q.write(enc_mp4)
    q.close()


def SM3sign(key):
    with open(key, 'r') as v:
        sm4key = v.read()
    v.close()
    res = SM3.Hash_sm3(sm4key)
    return res


def SM2encrypt(key, publickey):
    with open(key, 'r') as v:
        SM4key = v.read()
    v.close()
    with open(publickey, 'r') as w:
        pubkey = w.read()
    w.close()
    res = SM2.SM2Encrypt(SM4key, pubkey)
    return res


def init(SM4key, pubkey, now_time, path, videopath):
    sign = SM3sign(SM4key)
    enc_SM4key = bytes(SM2encrypt(SM4key, pubkey), encoding='utf-8')
    sign = bytes(sign, encoding='utf-8')
    # 写入encryption
    encryption = enc_SM4key + sign
    # print(enc_SM4key)
    # print(len(enc_SM4key))
    # print(sign)
    # print(len(sign))
    # print(encryption[:-64])
    mkdir(path + now_time + '\\')
    with open(path + now_time + '/enqcryption', 'wb') as w:
        w.write(encryption)
    w.close()
    #encryptMP4(videopath + now_time + '.mp4', SM4key, path)
    # cmod = 'gmssl sms4 -in '+ videopath + now_time + '.mp4'+' -out '+path + 'testmp4.enc'
    # os.system(cmod)
    # with open(SM4key, 'rb') as v:
    #     sm4key = v.read()
    # v.close()
    # os.system(sm4key)
    jarpath = os.path.join(os.path.abspath('.'), 'C:/Users/zh200/Desktop/树莓派py代码/SM4.jar')
    jpype.startJVM("C:/Program Files/Java/jdk1.8.0_152/jre/bin/server/jvm.dll", "-ea", "-Djava.class.path=%s" % jarpath)
    jpype.attachThreadToJVM()
    JClass = jpype.JClass('test.SM4')
    instance = JClass()
    instance.decode(videopath + now_time + '.mp4', SM4key)


def convert_to_mp4(source_path, target_path):
    cmod = 'MP4Box -add ' + source_path + ' -new ' + target_path
    execute_state = os.system('MP4Box -add ' + source_path + ' -new ' + target_path)
    print(cmod)
    print(execute_state)
    if execute_state == 0:
        return True
    else:
        return False


def gen7z(name, path):
    cmod = '7z a -t7z -r ' + name + '.7z ' + path + '*'
    execute_state = os.system(cmod)
    print(execute_state)
    if execute_state == 0:
        return True
    else:
        return False


def upload_init(host, user, passwd, p):
    global hostname, username, password, port
    hostname = host
    username = user
    password = passwd
    port = p


'''
上传函数
'''


def upload(local_dir, target_dir):
    try:
        # 设置ssh连接的远程ip以及端口
        t = paramiko.Transport((hostname, port))
        # 设置登录名以及密码
        t.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        # 读取文件路径
        sftp.put(local_dir, target_dir)
        t.close()
    except Exception as e:
        print(e)


class MyThread(threading.Thread):
    def __init__(self, now_time, SM4key, pubkey, prikey, path, videopath):
        threading.Thread.__init__(self)
        self.now_time = now_time
        self.SM4key = SM4key
        self.pubkey = pubkey
        self.prikey = prikey
        self.path = path
        self.videopath = videopath

    def run(self):
        #convert_to_mp4(self.videopath + now_time + '.h264', self.videopath + now_time + '.mp4')
        init(self.SM4key, self.pubkey, self.now_time, self.path, self.videopath)
        #gen7z(self.now_time, self.path + self.now_time)
        #upload(self.now_time + '.7z', "/home/ubuntu/mp4_enc/" + self.now_time + '.7z')


# 生成SM4密钥
def genSM4Key():
    res = str(uuid.uuid4())
    res = res.replace('-', '')
    SM4Key = bytes(res[:16].upper(), encoding='utf-8')
    with open('SM4KEY', 'wb') as w:
        w.write(SM4Key)
    w.close()


if __name__ == '__main__':
    genSM4Key()
    upload_init("119.29.86.218", "ubuntu", "FIATpcam2019", 22)
    camera = PiCamera()
    initvideopath = "./Video\\"
    initpath = "./Resource\\"
    mkdir(initvideopath)
    mkdir(initpath)
    while 1:
        path = "./Resource/"
        videopath = "./Video/"
        genSM4Key()
        now_time = dt.datetime.now().strftime('%F-%T')
        now_time = now_time.replace(":", "-")
        # print "开始录制"
        camera.resolution = (640,480)
        # camera.start_preview()
        filename = videopath + now_time + '.h264'
        camera.start_recording(filename)
        sleep(180)
        camera.stop_recording()
        # print "结束录制"
        print(now_time)
        # camera.stop_preview()
        # t = MyThread(filename)
        # 转码，加密，压缩，上传写在一个线程中
        # thread.start_new_thread(convert_to_mp4, (now_time+'.h264', now_time+'.mp4', ))
        SM4key = './SM4KEY'
        pubkey = './Pubkey'
        prikey = './Prikey'
        t = MyThread(now_time, SM4key, pubkey, prikey, path, videopath)
        t.start()


