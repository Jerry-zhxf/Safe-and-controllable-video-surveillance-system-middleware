# -*-coding: utf-8 -*-
from random import choice

# 选择素域，设置椭圆曲线参数
sm2_N = int('FFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFF7203DF6B21C6052B53BBF40939D54123', 16)
sm2_P = int('FFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000FFFFFFFFFFFFFFFF', 16)
sm2_G = '32C4AE2C1F1981195F9904466A39C9948FE30BBFF2660BE1715A4589334C74C7BC3736A2F4F6779C59BDCEE36B692153D0A9877CC62A474002DF32E52139F0A0'  # G��
sm2_a = int('FFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000FFFFFFFFFFFFFFFC',16)
sm2_b = int('28E9FA9E9D9F5E344D5A9E4BCF6509A7F39789F515AB8F92DDBCBD414D940E93',16)
sm2_a_3 = (sm2_a + 3) % sm2_P # 倍点用到的中间值
Fp = 256

def get_random_str(strlen): #随机产生字符串
    letterlist = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    str = ''
    for i in range(strlen):
        a = choice(letterlist)
        str = '%s%s' % (str,a)
    return str

def kG(k, Point,len_para):  # kP运算
    Point = '%s%s' % (Point, '1')
    mask_str = '8'
    for i in range(len_para-1):
        mask_str += '0'
    # print(mask_str)
    mask = int(mask_str, 16)
    Temp = Point
    flag = False
    for n in range(len_para * 4):
        if (flag):
            Temp = DoublePoint(Temp,len_para)
        if (k & mask) != 0:
            if (flag):
                Temp = AddPoint(Temp, Point,len_para)
            else:
                flag = True
                Temp = Point
        k = k << 1
    return ConvertJacb2Nor(Temp,len_para)

def DoublePoint(Point,len_para): # 倍点
    l = len(Point)
    len_2 = 2 * len_para
    if l< len_para*2:
        return None
    else:
        x1 = int(Point[0:len_para], 16)
        y1 = int(Point[len_para:len_2], 16)
        if l == len_2:
            z1 = 1
        else:
            z1 = int(Point[len_2:], 16)
        T6 = (z1 * z1) % sm2_P
        T2 = (y1 * y1) % sm2_P
        T3 = (x1 + T6) % sm2_P
        T4 = (x1 - T6) % sm2_P
        T1 = (T3 * T4) % sm2_P
        T3 = (y1 * z1) % sm2_P
        T4 = (T2 * 8) % sm2_P
        T5 = (x1 * T4) % sm2_P
        T1 = (T1 * 3) % sm2_P
        T6 = (T6 * T6) % sm2_P
        T6 = (sm2_a_3 * T6) % sm2_P
        T1 = (T1 + T6) % sm2_P
        z3 = (T3 + T3) % sm2_P
        T3 = (T1 * T1) % sm2_P
        T2 = (T2 * T4) % sm2_P
        x3 = (T3 - T5) % sm2_P

        if (T5 % 2) == 1:
            T4 = (T5 + ((T5 + sm2_P) >> 1) - T3) % sm2_P
        else:
            T4 = (T5 + (T5 >> 1) - T3) % sm2_P

        T1 = (T1 * T4) % sm2_P
        y3 = (T1 - T2) % sm2_P

        form = '%%0%dx' % len_para
        form = form * 3
        return form % (x3, y3, z3)

def AddPoint(P1, P2,len_para):  # 点加函数，P2点为仿射坐标即z=1，P1为Jacobian加重射影坐标
    len_2 = 2 * len_para
    l1 = len(P1)
    l2 = len(P2)
    if (l1 < len_2) or (l2 < len_2):
        return None
    else:
        X1 = int(P1[0:len_para], 16)
        Y1 = int(P1[len_para:len_2], 16)
        if (l1 == len_2):
            Z1 = 1
        else:
            Z1 = int(P1[len_2:], 16)
        x2 = int(P2[0:len_para], 16)
        y2 = int(P2[len_para:len_2], 16)

        T1 = (Z1 * Z1) % sm2_P
        T2 = (y2 * Z1) % sm2_P
        T3 = (x2 * T1) % sm2_P
        T1 = (T1 * T2) % sm2_P
        T2 = (T3 - X1) % sm2_P
        T3 = (T3 + X1) % sm2_P
        T4 = (T2 * T2) % sm2_P
        T1 = (T1 - Y1) % sm2_P
        Z3 = (Z1 * T2) % sm2_P
        T2 = (T2 * T4) % sm2_P
        T3 = (T3 * T4) % sm2_P
        T5 = (T1 * T1) % sm2_P
        T4 = (X1 * T4) % sm2_P
        X3 = (T5 - T3) % sm2_P
        T2 = (Y1 * T2) % sm2_P
        T3 = (T4 - X3) % sm2_P
        T1 = (T1 * T3) % sm2_P
        Y3 = (T1 - T2) % sm2_P

        form = '%%0%dx' % len_para
        form = form * 3
        return form % (X3, Y3, Z3)

def ConvertJacb2Nor(Point,len_para): # Jacobian加重射影坐标转换成仿射坐标
    len_2 = 2 * len_para
    x = int(Point[0:len_para], 16)
    y = int(Point[len_para:len_2], 16)
    z = int(Point[len_2:], 16)
    # z_inv = Inverse(z, P)
    z_inv = pow(z, sm2_P - 2, sm2_P)
    z_invSquar = (z_inv * z_inv) % sm2_P
    z_invQube = (z_invSquar * z_inv) % sm2_P
    x_new = (x * z_invSquar) % sm2_P
    y_new = (y * z_invQube) % sm2_P
    z_new = (z * z_inv) % sm2_P
    if z_new == 1:
        form = '%%0%dx' % len_para
        form = form * 2
        return form % (x_new, y_new)
    else:
        print ("Point at infinity!!!!!!!!!!!!")
        return None

def genSM2Key():
    len_para = int(Fp / 4)
    #print(len_para)
    d = get_random_str(len_para)  # 私钥
    # d = '3945208F7B2144B13F36E38AC6D39F95889393692860B51A42FB81EF4DF7C5B8'
    Pa = kG(int(d, 16), sm2_G, len_para).upper()  # 公钥
    print('公钥:' + Pa)
    f1 = open('Pubkey', 'w', encoding='utf8')
    f1.write(Pa)
    f1.close()
    print('私钥:' + d)
    f2 = open('Prikey', 'w', encoding='utf8')
    f2.write(d)
    f2.close()

if __name__=='__main__':
    genSM2Key()