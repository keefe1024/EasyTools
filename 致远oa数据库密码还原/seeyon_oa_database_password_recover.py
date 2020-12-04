# -*- coding: utf-8 -*-
# @Time    : 2020-12-04 15:40
# @Author  : Keefe
# @FileName: seeyon_oa_database_password_recover.py
# @Software: PyCharm
# @Blog    ：http://www.aiyuanzhen.com/
'''
致远oa数据库密码解密
使用说明:把配置文件中形如/1.0/xxxxxxxxxxxxxxxx那段提取出来然后运行py脚本
python seeyon_oa_database_password_recover.py /1.0/xxxxxxx=
'''
import re
import sys
import base64

def main():
    long_enc_pass = sys.argv[1]
    enc_pass= re.findall('/1.0/(.*)',long_enc_pass)
    print("解密前：" + long_enc_pass)
    data_pass = str(base64.b64decode(enc_pass[0]), "utf-8")
    pass_list=[]
    for i in data_pass:
        pass_list.append(chr(ord(i)-1))
    print("解密后：" + "".join(pass_list))
if __name__ == '__main__':
    main()