# -*- coding: utf-8 -*-
# @Time    : 2020-06-17 16:31
# @Author  : Keefe
# @FileName: social_work_dic.py
# @Software: PyCharm
# @Blog    ：http://www.aiyuanzhen.com/
'''
社工字典生成
'''
from itertools import combinations,permutations

email = "admin"  # emailname  admin@qq.com
phone = "13344556677"
name = "keefe"
domain = "aiyuanzhen"

common_pass_keywords ="!@#$%&*"
weak_passwords = ['123','1234']
social_info = [email,phone,name,domain]
dic_list = []
def common_dic():
    common_list = []
    for i in range(3):
        # 组合
        common_keywords = list(combinations(common_pass_keywords, i+1))
        for j in range(len(common_keywords)):
            common_list.append("".join(common_keywords[j]))
    return common_list




def social_dic():
    social_list = []
    for i in range(len(social_info)):
        social_info_keywords = list(permutations(social_info, i + 1))
        for j in range(len(social_info_keywords)):
            social_list.append("".join(social_info_keywords[j]))

    return social_list

def weak_dic():
    return weak_passwords

def all_dic():
    common = common_dic()
    weak = weak_dic()
    social = social_dic()
    for i in range(len(common)):
        for j in range(len(social)):
            for k in range(len(weak)):
                dic_list.append(common[i] + social[j] + weak[k])
                dic_list.append(common[i] + weak[k] + social[j])
                dic_list.append(social[j] + common[i] + weak[k])
                dic_list.append(social[j] + weak[k] + common[i])
                dic_list.append(weak[k] + social[j] + common[i])
                dic_list.append(weak[k] + common[i] + social[j])
    print(dic_list)
    print("总共：{} 条" .format(len(dic_list)))
    write_txt(dic_list)

def write_txt(dic_list):
    with open('social_dic.txt', 'a+',encoding='utf-8') as a:
        for i in range(len(dic_list)):
            a.write('{:}\n'.format(dic_list[i]))
    a.close()
    print("写入完成。")

def main():
    all_dic()
if __name__ == '__main__':
    main()