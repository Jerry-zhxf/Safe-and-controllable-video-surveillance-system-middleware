#!/usr/bin/python
import time

while(1):
	print("请输入您的选择：\n1.生成密钥\n2.解密文件\n3.发送证书请求\n4.退出")
	c = input()
	if c == '1':
		print("正在生成密钥")
		print("密钥生成成功")
	elif c == '2':
		print("请输入代解密文件名")
		x = input()
		print("请输入密钥文件名")
		y = input()
		print("开始解密")
		time.sleep(4)
		print("解密完成")
	elif c == '3':
		print("请选择密钥文件")
		a = input()
		print("正在获取设备指纹")
		print("请输入CA中心地址")
		b = input()
		time.sleep(3)
		
		print("请求发送成功")
		time.sleep(4)
		print("请求接收")
	else:
		exit(0)