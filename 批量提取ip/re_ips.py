# -*- coding: utf-8 -*-
# @Time    : 2020-12-12 01:36
# @Author  : Keefe
# @FileName: re-ips.py
# @Software: PyCharm
# @Blog    ：http://www.aiyuanzhen.com/
'''
批量提取ip
使用方法：
python re-ips.py xxx.txt
'''
import re
import sys

def main():
    
    with open(sys.argv[1],'r',encoding='utf-8')as f:
        #print(f.read())
        res = re.finditer(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])',f.read())
        for ip in res: 
            print (ip.group())
if __name__ == '__main__':
    main()