import uuid
def genSM4Key():
    res = str(uuid.uuid4())
    res = res.replace('-', '')
    SM4Key = bytes(res[:16].upper(), encoding='utf-8')
    with open('SM4Key','wb') as w:
        w.write(SM4Key)
    w.close()

genSM4Key()