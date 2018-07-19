#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

# 小于三个位置变量则退出脚本
if len(sys.argv) < 3:
    print("用法：python ./replace_file.py 项目中res文件夹的路径 存放下载的多语言文件的文件夹路径")
    sys.exit()

# 定义命名非法字符集&Java关键字集
invalid_key = ['/', ' ']
invalid_value = ['% {', '%d']
key_word = ['return', 'if']
# 设置三个位置变量
old_file, target_file = sys.argv[1], sys.argv[2]
# 打开需要替换的文件
f = open(old_file, 'wt')
# 清空当前文件内容
f.truncate(0)
# 打开新文件
f_new = open(target_file, 'r')
# 写xml头
f.writelines('<?xml version="1.0" encoding="utf-8"?>' + '\n')
f.writelines('<resources>' + '\n')

# 循环读取新文件
for line in f_new:
    if line.startswith('<string'):
        # 提取key并判断key的合法性
        start = line.index('"') + 1
        end = line.index('">')
        start1 = end + 1
        end1 = line.index('</string>')
        key = line[start:end]
        value = line[start1:end1]

        # 判断key是否是关键字
        if key in key_word:
            print(key)
            print('key不能是Java关键字：')
        else:
            valid = True
            # 判断key中否包含非法字符
            for text in invalid_key:
                if text in key:
                    print(key)
                    print('该key中包含非法字符：')
                    valid = False
                    break
            # 判断value中是否包含非法字符
            for text in invalid_value:
                if text in value:
                    print(value)
                    valid = False
                    break
            # key是合法的，替换value中需要转义的字符，例如英文中的'
            if valid:
                line = line.replace("\'", "\\'").replace("&", "&amp;")
                f.writelines(line)

f.writelines('\n')
f.writelines('<string name="imageview">imageView</string> \n')
f.writelines('<string name="icon_help">&#xe616;</string> \n' +
             '<string name="icon_arrow_down">&#xe612;</string> \n' +
             '<string name="icon_star_empty">&#xe60b;</string> \n' +
             '<string name="icon_flash_booking">&#xe617;</string> \n' +
             '<string name="icon_arrow_right">&#xe61a;</string> \n')
# 写xml结束标签
f.writelines('</resources>')
print('替换完成！')
f.close()
f_new.close()
