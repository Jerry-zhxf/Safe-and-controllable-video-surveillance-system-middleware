#coding = utf-8
import os
import paramiko
import datetime

'''
初始化连接的服务器的基本信息
'''
def init(host,user,passwd,p):
    global hostname,username,password,port
    hostname = host
    username = user
    password = passwd
    port = p

'''
上传函数
'''
def upload(local_dir,target_dir):
    try:
        #设置ssh连接的远程ip以及端口
        t = paramiko.Transport((hostname,port))
        #设置登录名以及密码
        t.connect(username=username,password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        #读取文件路径
        sftp.put(local_dir,target_dir)
        t.close()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    init("119.29.86.218", "ubuntu", "FIATpcam2019", 22)
    upload("C:/Users/zh200/Desktop/test.txt", "/home/ubuntu/mp4_enc/test.txt")