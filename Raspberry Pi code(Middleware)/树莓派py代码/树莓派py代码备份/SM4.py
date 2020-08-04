#coding = utf-8

from gmssl.sm4 import CryptSM4, SM4_ENCRYPT, SM4_DECRYPT

def encrypt(key:bytes,value:bytes):
	crypt_sm4 = CryptSM4()
	crypt_sm4.set_key(key, SM4_ENCRYPT)
	encrypt_value = crypt_sm4.crypt_ecb(value) #  bytes类型
	return encrypt_value