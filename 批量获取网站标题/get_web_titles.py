# -*- coding: utf-8 -*-
# @Time    : 2020-04-13 23:38
# @Author  : Keefe
# @FileName: get_web_titles.py
# @Software: PyCharm
# @Blog    ：http://www.aiyuanzhen.com/
'''
批量获取网站标题
'''
import requests
from lxml import etree
import threading
import logging
import re
from concurrent.futures import ThreadPoolExecutor # 使用线程池

lock = threading.Lock()

def write_jump_txt(url, title):
    lock.acquire()
    print(url + "\t----\t" + '\t----\t'.join(title))
    with open('3XX.txt', 'a+') as a:
        a.write(url)
        for i in title:
            a.write('\t----\t'+i)
        else:
            a.write('\n')
    lock.release()

def write_error_txt(url, title):
    lock.acquire()
    print(url + "\t----\t" + '\t----\t'.join(title))
    with open('5XX.txt', 'a+') as a:
        a.write(url)
        for i in title:
            a.write('\t----\t'+i)
        else:
            a.write('\n')
    lock.release()

def write_forbidden_txt(url, title):
    lock.acquire()
    print(url + "\t----\t" + '\t----\t'.join(title))
    with open('4XX.txt', 'a+') as a:
        a.write(url)
        for i in title:
            a.write('\t----\t'+i)
        else:
            a.write('\n')
    lock.release()

def write_success_txt(url, title):
    lock.acquire()
    print(url + "\t----\t" + '\t----\t'.join(title))
    with open('2XX.txt', 'a+') as a:
        a.write(url)
        for i in title:
            a.write('\t----\t'+i)
        else:
            a.write('\n')
    lock.release()

def get_title(url):
    # 设置请求头
    headers = {
        'Connection': 'close',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
    }
    # 发送get请求，移除SSL认证
    response = requests.get(url, headers=headers, timeout=5, verify=False)
    # 获取真实编码，统一编码字符集
    response.encoding = response.apparent_encoding
    # 获取解析结果
    tree = etree.HTML(response.text)
    title = tree.xpath('.//title/text()')
    if re.match('^4\d{2}$', str(response.status_code)):
        write_forbidden_txt(url, title)
    elif re.match('^5\d{2}$', str(response.status_code)):
        write_error_txt(url, title)
    elif re.match('^3\d{2}$', str(response.status_code)):
        write_jump_txt(url, title)
    else:
        write_success_txt(url,title)

def main():
    # 不捕获警告
    logging.captureWarnings(True)
    with ThreadPoolExecutor(max_workers=50) as executor:
        for line in open('domains.txt').readlines():
            executor.submit(get_title,line.strip('\n'))

if __name__ == '__main__':
    main()