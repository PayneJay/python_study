#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

# 小于三个位置变量则退出脚本
if len(sys.argv) < 3:
    print("useage: ./replace_file.py 需要替换的文件的路径 下载的新文件的路径")
    sys.exit()

# 定义命名非法字符集&Java关键字集
invalid_str = ['/', ' ']
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
        start = line.index('"') + 1
        end = line.index('">')
        key = line[start:end]
        # 判断是否包含关键字
        if key in key_word:
            print(key)
            print('key不能是Java关键字：')
        else:
            valid = True
            # 判断是否包含非法字符
            for text in invalid_str:
                if text in key:
                    print(key)
                    print('该key中包含非法字符：')
                    valid = False
                    break
            # 如果合法则写入
            if valid:
                # print(line)
                f.write(line)

# 写xml结束标签
f.write('</resources>')

f.close()
f_new.close()