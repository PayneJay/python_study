#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json
import sys
import os

# 小于三个位置变量则退出脚本
if len(sys.argv) < 2:
    print("用法：python3 ./python_requests.py 需要下载的环境（alpha/release)")
    sys.exit()

# 创建存放多语言文件的文件夹
language_dir = 'waka_languages'
os.makedirs(language_dir)

alpha_url = 'http://alpha-translate.fishtrip.cn/api/v2/language_dicts'
release_url = 'http://translate.fishtrip.cn/api/v2/language_dicts'
url = release_url if sys.argv[1] == 'release' else alpha_url


# 获取请求下载多语言文件的url地址
def get_url(local):
    # 默认url及参数
    payload = {
        'user_id': '',
        'login_string': '',
        'product': 'waka_app',
        'language_code': local,
        'end_code': '2',
        'local_version': ''
    }

    # 请求接口获取对应多语言文件的下载地址
    print(url + '\n')
    r = requests.get(url, params=payload)
    r.encoding = 'utf-8'
    new_dict = json.loads(r.text)
    print(new_dict["data"]["language_dict"] + '\n')
    return new_dict["data"]["language_dict"]


# 获取服务器多语言文件并写入本地文件
def load_write(path, url):
    f = open(path, 'wt', encoding='utf-8')

    # 获取WAKA中文简体多语言文件
    result = requests.get(url)
    # 清空当前文件内容
    f.truncate(0)
    result.encoding = 'utf-8'
    f.write(result.text)
    f.close()


# 中文简体
load_write(language_dir + '/language_zh-CN.xml', get_url('zh-CN'))

# 中文繁体
load_write(language_dir + '/language_zh-TW.xml', get_url('zh-TW'))

# 英文
load_write(language_dir + '/language_en.xml', get_url('en'))

# 日语
load_write(language_dir + '/language_ja-JP.xml', get_url('ja'))

# 韩语
load_write(language_dir + '/language_ko-KR.xml', get_url('ko'))

# 泰语
load_write(language_dir + '/language_th-TH.xml', get_url('th'))

# 越南语
load_write(language_dir + '/language_vi-VN.xml', get_url('vi'))
