#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys

# 小于三个位置变量则退出脚本
if len(sys.argv) < 3:
    print("用法：python ./waka_replace.py 项目中res文件夹的路径 存放下载的多语言文件的文件夹路径")
    sys.exit()

# 获取参数
target_path = sys.argv[1]
new_file_path = sys.argv[2]
# 替换泰语
os.popen('python replace_file.py ' + target_path + '/values-th/strings.xml ' +
         new_file_path + '/language_th-TH.xml')
print('替换泰语完成')
# 替换越南语
os.popen('python replace_file.py ' + target_path + '/values-vi/strings.xml ' +
         new_file_path + '/language_vi-VN.xml')
print('替换越南语完成')
# 替换韩语
os.popen('python replace_file.py ' + target_path + '/values-ko/strings.xml ' +
         new_file_path + '/language_ko-KR.xml')
print('替换越南语完成')
# 替换日语
os.popen('python replace_file.py ' + target_path + '/values-ja/strings.xml ' +
         new_file_path + '/language_ja-JP.xml')
print('替换日语完成')
# 替换英语
os.popen('python replace_file.py ' + target_path + '/values-en/strings.xml ' +
         new_file_path + '/language_en.xml')
print('替换英语完成')
# 替换繁体中文
os.popen('python replace_file.py ' + target_path +
         '/values-zh-rTW/strings.xml ' + new_file_path + '/language_zh-TW.xml')
print('替换繁体中文完成')
# 替换简体中文
os.popen('python replace_file.py ' + target_path +
         '/values-zh-rCN/strings.xml ' + new_file_path + '/language_zh-CN.xml')
print('替换简体中文完成')
# 替换默认语言
os.popen('python replace_file.py ' + target_path + '/values/strings.xml ' +
         new_file_path + '/language_zh-CN.xml')
print('替换默认语言完成')
