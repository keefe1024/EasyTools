# -*- coding: utf-8 -*-
# @Time    : 2020-11-08 12:46
# @Author  : Keefe
# @FileName: masscan_xml_to_xls.py
# @Software: PyCharm
# @Blog    ：http://www.aiyuanzhen.com/
'''
xml to xls
'''
# coding: utf-8

import bs4
import xlsxwriter
import argparse

# 读取xml文件，写入excel
def xmlToExcel(file_xml, file_excel):
    # 打开xml文件，并以此创建一个bs对象
    xml = open(file_xml, 'r')
    doc = bs4.BeautifulSoup(xml, 'xml')

    # 创建一个excel文件，并添加一个sheet，命名为orders
    workbook = xlsxwriter.Workbook(file_excel)
    sheet = workbook.add_worksheet('ip汇总')

    # 设置粗体
    bold = workbook.add_format({'bold': True})

    # 先在第一行写标题，用粗体
    sheet.write('A1', u'IP', bold)
    sheet.write('B1', u'端口', bold)
    sheet.write('C1', u'addrtype', bold)
    sheet.write('D1', u'protocol', bold)
    sheet.write('E1', u'state', bold)
    sheet.write('F1', u'reason', bold)
    sheet.write('G1', u'reason_ttl', bold)
    sheet.write('H1', u'serive', bold)
    sheet.write('I1', u'banner', bold)

    # 筛选出所有的<host>，这里使用的是CSS选择器
    host = doc.select('host')

    # 行号，具体ip信息从第二行开始
    row = 2
    # 将每一个host写入excel
    for x in host:
        # 提取出具体信息
        ip = x.address["addr"]
        ports = x.port["portid"]
        add_type = x.address["addrtype"]
        protocols = x.port["protocol"]
        states = x.state["state"]
        reasons = x.state["reason"]
        reason_ttls = x.state["reason_ttl"]
        try:
            service_names = x.service["name"]
            banners = x.service["banner"]
        except TypeError:
            pass
        # 将具体信息写入excel
        sheet.write('A%d' % row, ip)
        sheet.write('B%d' % row, ports)
        sheet.write('C%d' % row, add_type)
        sheet.write('D%d' % row, protocols)
        sheet.write('E%d' % row, states)
        sheet.write('F%d' % row, reasons)
        sheet.write('G%d' % row, reason_ttls)
        try:
            sheet.write('H%d' % row, service_names)
            sheet.write('I%d' % row, banners)
        except UnboundLocalError:
            sheet.write('H%d' % row, "")
            sheet.write('I%d' % row, "")

        row += 1

    # 关闭文件
    xml.close()
    workbook.close()

# 测试代码
def main():
    parser = argparse.ArgumentParser(description="masscan xml格式转xlsx")
    parser.add_argument('-x', '--xml', default="scan.xml")
    parser.add_argument('-o', '--output', default="scan.xlsx")
    args = parser.parse_args()
    xml = args.xml
    output = args.output

    xmlToExcel(xml, output)


if __name__ == '__main__':
    main()