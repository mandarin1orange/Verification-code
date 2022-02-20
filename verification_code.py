#! /usr/bin/python
# -*- coding: UTF-8 -*-

# 生成验证码小程序

import random

def v_code():
    code = ''
    for i in range(4):
        num = random.randint(0,9)
        alf = chr(random.randint(65,90))  # chr(65) = A，简而言之 A-Z随机生成
        add = random.choice([num,alf])  # 在0-9数字和A-Z字母中随便选一个
        code = ''.join([code,str(add)])  # 加入到code里面
    return code

def main():
    yzm = v_code()
    print(yzm)
    pass

if __name__ == '__main__':
    main()