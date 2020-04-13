# -*- coding: utf-8 -*-
# @Time    : 2020-03-27 3:08
# @Author  : Keefe
# @FileName: pinyin_conversion.py
# @Software: PyCharm
# @Blog    ：http://www.aiyuanzhen.com/
'''
批量中文转拼音（fuzz人名爆破）
'''
from pypinyin import lazy_pinyin

def main():
    with open('inFile.txt', 'rb') as a:
        with open('outFile.txt', 'wb') as b:
            for line in a.readlines():
                a = line.decode().strip("\n")
                pinyin_outfile = "".join(str(x) for x in lazy_pinyin(a))
                b.write(pinyin_outfile.encode())

if __name__ == '__main__':
    main()
