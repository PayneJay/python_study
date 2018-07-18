#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

# 替换泰语
os.popen(
    'python replace_file.py /Users/weipengjie/Documents/workspace/wakaandroidstudio/wakaAndroid/src/main/res/values-th/strings.xml /Users/weipengjie/Desktop/waka_language/language_th.xml'
)
print('替换泰语完成')
# 替换越南语
os.popen(
    'python replace_file.py /Users/weipengjie/Documents/workspace/wakaandroidstudio/wakaAndroid/src/main/res/values-vi/strings.xml /Users/weipengjie/Desktop/waka_language/language_vi.xml'
)
print('替换越南语完成')
# 替换韩语
os.popen(
    'python replace_file.py /Users/weipengjie/Documents/workspace/wakaandroidstudio/wakaAndroid/src/main/res/values-ko/strings.xml /Users/weipengjie/Desktop/waka_language/language_ko.xml'
)
print('替换越南语完成')
# 替换日语
os.popen(
    'python replace_file.py /Users/weipengjie/Documents/workspace/wakaandroidstudio/wakaAndroid/src/main/res/values-ja/strings.xml /Users/weipengjie/Desktop/waka_language/language_ja.xml'
)
print('替换日语完成')
# 替换英语
os.popen(
    'python replace_file.py /Users/weipengjie/Documents/workspace/wakaandroidstudio/wakaAndroid/src/main/res/values-en/strings.xml /Users/weipengjie/Desktop/waka_language/language_en.xml'
)
print('替换英语完成')
# 替换繁体中文
os.popen(
    'python replace_file.py /Users/weipengjie/Documents/workspace/wakaandroidstudio/wakaAndroid/src/main/res/values-zh-rTW/strings.xml /Users/weipengjie/Desktop/waka_language/language_zhTW.xml'
)
print('替换繁体中文完成')
# 替换简体中文
os.popen(
    'python replace_file.py /Users/weipengjie/Documents/workspace/wakaandroidstudio/wakaAndroid/src/main/res/values-zh-rCN/strings.xml /Users/weipengjie/Desktop/waka_language/language_zhCN.xml'
)
print('替换简体中文完成')
# 替换默认语言
os.popen(
    'python replace_file.py /Users/weipengjie/Documents/workspace/wakaandroidstudio/wakaAndroid/src/main/res/values/strings.xml /Users/weipengjie/Desktop/waka_language/language_zhCN.xml'
)
print('替换默认语言完成')
