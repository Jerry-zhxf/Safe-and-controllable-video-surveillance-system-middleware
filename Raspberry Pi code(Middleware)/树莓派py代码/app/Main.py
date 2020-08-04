import os
import paramiko
import datetime
import base64
import binascii
import SM2
import SM3
import jpype
from jpype import *



'''
SM2加密解密
'''


'''
SM3签名
'''

def SM3signit(value):
    #value为bytes类型
    res = sm3.sm3_hash(func.bytes_to_list(value))
    res = bytes(res,'utf-8')  
    return res


'''
解密文件部分
参数1--------->密钥
参数2--------->待解密文件(bytes格式)
'''

def SM4decrypt(key,value):
    crypt_sm4 = CryptSM4()
    #调用SM4算法model
    crypt_sm4.set_key(key, SM4_DECRYPT)
    #利用cbc模式进行解密
    decrypt_value = crypt_sm4.crypt_ecb(value)  # bytes类型
    #返回解密后的值
    return decrypt_value

'''
SM3验证函数
'''

def verify(value,sign):
    l = len(sign)
    value_sm3 = SM3.Hash_sm3(value)
    for i in range(64):
        if value_sm3[i]!=sign[i]:
            return 0
    return 1

'''
SM2解密加密后的密钥并验证
验证通过后利用得到的密钥解密加密后的视频
选取mp4和key的路径(str类型)
选取公钥、私钥(str类型)
解密value(bytes类型)
调用verify函数验证签名,验证不通过返回0，通过返回密钥(bytes类型)
'''
def mp4decrypt(mp4_file:str,key_file:str,userprikey:str):
    with open(key_file,'r') as v:
        value = v.read()
    v.close()
    #签名校验值
    sign = value[-64:]
    #加密后的密钥
    value = value[:-64]
    with open(userprikey,'r') as pr:
        prikey = pr.read()
    pr.close()
    res =  SM2.SM2Decrypt(value,prikey)
    if verify(res,sign) == 0:
        print('密钥文件被篡改')
        return 0
    else:
        with open('./SM4key', 'w') as w:
            w.write(res)
        w.close()
        jarpath = os.path.join(os.path.abspath('.'), 'C:/Users/zh200/Desktop/app/SM4.jar')
        jpype.startJVM("C:/Program Files/Java/jdk1.8.0_131/jre/bin/server/jvm.dll", "-ea", "-Djava.class.path=%s" % jarpath)
        jpype.attachThreadToJVM()
        JClass = jpype.JClass('test.SM4')
        instance = JClass()
        SM4KEY = './SM4key'
        instance.decode(mp4_file, SM4KEY)
        # with open(mp4_file,'rb') as v:
        #     value = v.read()
        # v.close()
        # mp4 = SM4decrypt(res,value)
        # with open('res.mp4','wb') as w:
        #     w.write(mp4)
        # w.close()

def getencrypt(mp4_file:str,key_file:str,userprikey:str):
    mp4decrypt(mp4_file,key_file,userprikey)

'''
初始化连接的服务器的基本信息
'''
def init(host,user,passwd):
    global hostname,username,password,port
    hostname = host
    username = user
    password = passwd
    port = 22

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

def file_up(host:str,name:str,passwd:str,file:str,key:str):
    # 第一步 初始化连接信息
    init(host, name, passwd)
    # 第二步 确定上传文件路径
    # 第三步 确定最终上传后的文件路径
    target_file = '/home/ubuntu/pcamtest/' + 'request'
    # 第四步 上传
    with open(file,'r') as w:
        value = w.read()
    w.close()
    #print(value)
    with open(key,'r') as v:
        key = v.read()
    v.close()
    #print(key)
    res = SM2.SM2Encrypt(value,key)
    sign = SM3.Hash_sm3(value)
    ans = res+sign
    with open('request','w') as x:
        x.write(ans)
    x.close()
    upload('request', target_file)


'''
上传文件测试部分
**参数意义**
ip
用户名
密码
上传的文件本地路径
'''
'''global hos,nam,paswd,tar
hos = '119.29.86.218'
nam = 'ubuntu'
paswd = 'FIATpcam2019'
file = 'SM4.py'

file_up(hos,nam,paswd,file)
'''


'''
解密文件
'''
'''
def getencrypt(mp4_file:str,key_file:str,userprikey:str,userpubkey:str):
    userpubkey = userprikey[:-10]+'PubKey'
    mp4decrypt(mp4_file,key_file,userpubkey,userprikey)
    
mp4_file = '/Users/zhd/Desktop/Fiat作品赛/作品构建/PC_app/venv/include/test/encrypt/testmp4.enc'
key_file = '/Users/zhd/Desktop/Fiat作品赛/作品构建/PC_app/venv/include/test/encrypt/encryption'
userprikey = '/Users/zhd/Desktop/Fiat作品赛/作品构建/PC_app/venv/include/test/encrypt/PrivateKey'
userpubkey = userprikey[:-10]+'PubKey'
mp4decrypt(mp4_file,key_file,userpubkey,userprikey)
'''