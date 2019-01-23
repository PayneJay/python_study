#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys

# /Users/weipengjie/Documents/workspace/wakaandroidstudio/wakaAndroid/src/main/res
# 小于三个位置变量则退出脚本
if len(sys.argv) < 2:
    print("用法：python ./waka_replace.py 项目中res文件夹的路径")
    sys.exit()

# 获取参数
base_path = sys.argv[1]
target_path = os.getcwd() + '/waka_languages'


# 执行replace_file.py脚本
def executive(other_path, file_name):
    os.popen('python3 ' + os.getcwd() + '/replace_file.py' + ' ' + base_path +
             other_path + ' ' + target_path + file_name)
    print('{} 替换完成'.format(other_path))


# 替换泰语
executive('/values-th/strings.xml', '/language_th-TH.xml')
# 替换越南语
executive('/values-vi/strings.xml', '/language_vi-VN.xml')
# 替换韩语
executive('/values-ko/strings.xml', '/language_ko-KR.xml')
# 替换日语
executive('/values-ja/strings.xml', '/language_ja-JP.xml')
# 替换英语
executive('/values-en/strings.xml', '/language_en.xml')
# 替换繁体中文
executive('/values-zh-rTW/strings.xml', '/language_zh-TW.xml')
# 替换简体中文
executive('/values-zh-rCN/strings.xml', '/language_zh-CN.xml')
# 替换默认语言
executive('/values/strings.xml', '/language_zh-CN.xml')
