'''
Author: sunshaochen 805960031@qq.com
Date: 2022-09-20 11:15:02
LastEditors: sunshaochen 805960031@qq.com
LastEditTime: 2022-09-22 16:37:12
FilePath: \learn-python3-the-hard-way\2_Advance\字符串字节字符编码.py
Description: 主要功能是将文字编码和解码。
'''

import sys
script, encoding, error = sys.argv 


def main(language_file, encoding, errors):  # 定义主函数
    line = language_file.readline()        #读取文件里一行

    if line:                                #判断若 line 不是空字符串，则执行下面
        print_line(line, encoding, errors)  # 执行函数
        return main(language_file, encoding, errors)    # 递归执行 main函数


def print_line(line, encoding, errors): # 定义函数 
    next_lang = line.strip()        # strip函数删除line字符串的前后空格。
    raw_bytes = next_lang.encode(encoding, errors=errors)   #encode 编码 
    cooked_string = raw_bytes.decode(encoding, errors=errors) #decode 解码

    print(raw_bytes, "<===>", cooked_string) 


languages = open("languages.txt", encoding="utf-8")  

main(languages, encoding, error)  # 调用