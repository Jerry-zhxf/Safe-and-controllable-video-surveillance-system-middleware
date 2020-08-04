#coding = utf-8

import base64
import binascii
from gmssl import sm2, func

def encrypt(pubkey,prikey,value):
    sm2_crypt = sm2.CryptSM2(public_key=pubkey, private_key=prikey)
    enc_value = sm2_crypt.encrypt(value)
    return enc_value

def decrypt(pubkey,prikey,value):
    sm2_crypt = sm2.CryptSM2(public_key=pubkey, private_key=prikey)
    dec_value = sm2_crypt.decrypt(value)
    return dec_value
