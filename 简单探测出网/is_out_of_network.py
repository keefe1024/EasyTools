# -*- coding: utf-8 -*-
# @Time    : 2020-03-26 1:08
# @Author  : Keefe
# @FileName: is_out_of_network.py
# @Software: PyCharm
# @Blog    ：http://www.aiyuanzhen.com/
'''
简单判断是否出网
'''
import socket
import re
import requests
import os
import threading


def is_tcp_out_network():
    # 创建一个socket:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接:
    s.connect(('www.baibu.com', 80))
    # 发送数据:
    s.send(b'GET / HTTP/1.1\r\nHost: www.baibu.com\r\nConnection: close\r\n\r\n')
    # 接收数据:
    buffer = []
    while True:
        # 每次最多接收1k字节:
        d = s.recv(1024)
        if d:
            buffer.append(d)
        else:
            break
    data = b''.join(buffer)
    # 关闭连接:
    s.close()
    if (re.match('HTTP/1.1 200 OK', data.decode())):
        print("TCP出网")
    else:
        print("TCP不出网")


def is_http_out_network():
    response = requests.get("http://www.baidu.com/")
    if (response.status_code == 200):
        print("HTTP出网")
    else:
        print("HTTP不出网")


def is_icmp_out_network():
    command = 'ping www.baidu.com'
    result = os.popen(command)
    res = result.read()

    if (re.search('TTL=', res)):
        print("ICMP出网")
    else:
        print("ICMP不出网")


def is_dns_out_network():
    command = 'nslookup www.baidu.com 8.8.8.8'
    result = os.popen(command)
    res = result.read()

    if (re.search('Aliases:', res)):
        print("DNS出网")
    else:
        print("DNS不出网")


def main():
    t1 = threading.Thread(target=is_tcp_out_network)
    t2 = threading.Thread(target=is_http_out_network)
    t3 = threading.Thread(target=is_dns_out_network)
    t4 = threading.Thread(target=is_icmp_out_network)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    input()


if __name__ == "__main__":
    main()