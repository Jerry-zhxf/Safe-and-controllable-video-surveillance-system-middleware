#coding = utf-8
import SM2,SM3,SM4
def encryptMP4(file:str,key:str):
    with open(file,'rb') as v:
        value = v.read()
    v.close()
    with open(key,'rb') as w:
        sm4key = w.read()
    w.close()
    enc_mp4 = SM4.encrypt(sm4key,value)
    with open('testmp4.enc','wb') as q:
        q.write(enc_mp4)
    q.close()

def SM3sign(key:str):
    with open(key,'rb') as v:
        sm4key = v.read()
    v.close()
    res = SM3.signit(sm4key)
    return res

def SM2encrypt(key:str,publickey:str,privatekey:str):
    with open(key,'rb') as v:
        SM4key = v.read()
    v.close()
    with open(publickey,'r') as w:
        pubkey = w.read()
    w.close()
    with open(privatekey,'r') as q:
        prikey = q.read()
    q.close()
    res = SM2.encrypt(pubkey,prikey,SM4key)
    return res

def SM2decrypt(key:str,publickey:str,privatekey:str):
    with open(key,'rb') as v:
        SM4enc_key = v.read()[:-64]
    v.close()
    with open(publickey,'r') as w:
        pubkey = w.read()
    w.close()
    with open(privatekey,'r') as q:
        prikey = q.read()
    q.close()
    res = SM2.decrypt(pubkey,prikey,SM4enc_key)
    return res

def init(SM4key:str,pubkey:str,prikey:str,testmp4:str):
    sign = SM3sign(SM4key)
    enc_SM4key = SM2encrypt(SM4key,pubkey,prikey)
    sign = bytes(sign, encoding='utf-8')
    #写入encryption
    encryption = enc_SM4key + sign
    # print(enc_SM4key)
    # print(len(enc_SM4key))
    # print(sign)
    # print(len(sign))
    # print(encryption[:-64])
    with open('encryption','wb') as w:
        w.write(encryption)
    w.close()
    encryptMP4(testmp4,SM4key)


if __name__ == '__main__':
    SM4key = 'C:/Users/zh200/Desktop/树莓派py代码/SM4KEY.txt'
    pubkey = 'C:/Users/zh200/Desktop/树莓派py代码/pubkeytest'
    prikey = 'C:/Users/zh200/Desktop/树莓派py代码/prikeytest'
    testmp4 = 'C:/Users/zh200/Desktop/树莓派py代码/test.mp4'
    #enc_sm4 = 'C:/Users/zh200/Desktop/树莓派py代码/encryption'
    #print(SM2decrypt(enc_sm4, pubkey, prikey))

    init(SM4key,pubkey,prikey,testmp4)