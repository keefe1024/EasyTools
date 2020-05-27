# -*- coding: utf-8 -*-
# @Time    : 2020-05-27 23:50
# @Author  : Keefe
# @FileName: tcp_explore_port.py
# @Software: PyCharm
# @Blog    ：http://www.aiyuanzhen.com/
'''
批量TCP探测端口开放
ip格式
1.2.3.4:80
'''
import socket
import threading
import logging
from concurrent.futures import ThreadPoolExecutor # 使用线程池

lock = threading.Lock()

def load_file(dir):
    ip_list=[]
    for line in open(dir,'r').readlines():
        i = line.strip('\n')
        str_list = line.split(" ")
        ip_list.append(str_list)
    return ip_list
            # return str_list[0], str_list[1]


def write_open_txt(tgthost, tgtport):
    lock.acquire()
    with open('open.txt', 'a+') as a:
        a.write('[+] %s..%d/tcp open\n' % (tgthost, tgtport))
    lock.release()

def write_close_txt(tgthost, tgtport):
    lock.acquire()
    with open('close.txt', 'a+') as a:
        a.write('[-]%s..%d/tcp close\n'%(tgthost,tgtport))
    lock.release()

def connscan(tgthost,tgtport):
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((tgthost,tgtport))
        print('[+] %s..%d/tcp open' % (tgthost, tgtport))
        write_open_txt(tgthost, tgtport)
        s.close()
    except:
        print('[-]%s..%d/tcp close' % (tgthost, tgtport))
        write_close_txt(tgthost,tgtport)


if __name__ == '__main__':
    dir = "ips.txt"
    str_list = load_file(dir)
    # 不捕获警告
    logging.captureWarnings(True)
    with ThreadPoolExecutor(max_workers=50) as executor:
        for x,y in str_list:
            executor.submit(connscan,x,int(y))

