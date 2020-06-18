# -*- coding: utf-8 -*-
# @Time    : 2020-06-18 22:43
# @Author  : Keefe
# @FileName: line_add_key.py
# @Software: PyCharm
# @Blog    ：http://www.aiyuanzhen.com/
'''
文本行后追加指定字符串
'''
def dispose_add_key(key):
    with open('lines.txt', 'r') as a:
        for line in a.readlines():
            new_line = line.strip("\n") + str(key)
            write_txt(new_line)
    a.close()

def write_txt(new_line):
    with open('new_lines.txt','a+') as b:
        b.write(new_line+"\n")
    b.close()

def main():
    key = "@qq.com"
    dispose_add_key(key)

if __name__ == '__main__':
    main()
