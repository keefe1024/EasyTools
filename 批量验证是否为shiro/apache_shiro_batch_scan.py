# -*- coding: utf-8 -*-
# @Time    : 2020-10-22 15:40
# @Author  : Keefe
# @FileName: apache_shiro_batch_scan.py
# @Software: PyCharm
# @Blog    ：http://www.aiyuanzhen.com/
'''
批量验证是否为shiro
'''
import os
import requests
import threading
import logging
from concurrent.futures import ThreadPoolExecutor
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# 禁用安全请求警告
lock = threading.Lock()

def poc(url):
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163'
    headers['Cookie'] = 'rememberMe=1'
    line_url = url.strip()    # 每行去空格
    flag = 0
    res = requests.get(line_url, headers=headers, timeout=3, verify=False, allow_redirects=False)    # 发送GET验证请求
    if 'Set-Cookie' in res.headers:
        if 'deleteMe' not in res.headers['Set-Cookie']:    # 判断响应包Set-Cookie中是否有deleteMe字样
            flag = 0
        else:
            flag = 1
    else:
        flag = 0

    if flag == 0:    # 如果GET请求获取不到信息，尝试POST请求获取信息
        res2 = requests.post(line_url, headers=headers, timeout=3, verify=False, allow_redirects=False)    # 发送POST验证请求
        if 'Set-Cookie' in res2.headers:
            if 'deleteMe' not in res2.headers['Set-Cookie']:    # 判断响应包Set-Cookie中是否有deleteMe字样
                flag = 0
            else:
                flag = 1
        else:
            flag = 0

    if flag == 1:
        print("[-]{} - 可能是shiro".format(line_url))
    elif flag == 0:
        print("[-]{} - 可能不是shiro".format(line_url))
    else:
        print("[-]{} - 可能出现了某种错误".format(line_url))

def main():
    f = open('url.txt','r')
    # url格式，携带http://   or   https://
    # 不捕获警告
    logging.captureWarnings(True)
    with ThreadPoolExecutor(max_workers=50) as executor:
        for line in f.readlines():
            executor.submit(poc,line)

if __name__ == '__main__':
    main()