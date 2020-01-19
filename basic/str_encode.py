#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
好了里面全是注释
"""

x = 'nihao'
bx = x.encode('utf-8')  # 网络传输的时候需要转换为bytes
z = bx.decode('utf-8', errors='ignore')
# 重新解码
b = ord('$')  # 将字符转为编码
c = chr(36)  # 将编码转化为字符
print(z, c, b)
s1 = "你好今天我想吃%d个%s" % (2,'橙子')
print(s1)
