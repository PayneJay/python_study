#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import random
# import time
import requests
import json
from pyecharts import Geo


# 爬取🍅数据
def get_tomato_data():
    tomato = pd.DataFrame(columns=['date', 'score', 'city', 'comment', 'nick'])
    for i in range(0, 500):
        j = random.randint(0, 500)
        print(str(i) + '    ' + str(j))
        try:
            # time.sleep(1)
            url = 'http://m.maoyan.com/mmdb/comments/movie/1212592.json?_v_=yes&offset=' + str(
                j)
            html = requests.get(url).content
            data = json.loads(html.decode('utf-8'))['cmts']

            for item in data:
                tomato = tomato.append(
                    {
                        'date': item['time'].split(' ')[0],
                        'city': item['cityName'],
                        'score': item['score'],
                        'comment': item['content'],
                        'nick': item['nick']
                    },
                    ignore_index=True)
            tomato.to_csv('西虹市首富4.csv', index=False)
        except ValueError:
            continue


# 过滤掉重复的数据
def filter_repeat(infile, outfile):
    inopen = open(infile, 'r', encoding='utf-8')
    outopen = open(outfile, 'w', encoding='utf-8')
    lines = inopen.readlines()
    list_1 = []
    for line in lines:
        if line not in list_1:
            list_1.append(line)
            outopen.writelines(line)
    inopen.close()
    outopen.close()


# 热力图
def thermodynamic_chart():
    tomato_com = pd.read_excel('西虹市首富.xlsx')
    grouped = tomato_com.groupby(['city'])
    grouped_pct = grouped['score']
    # tip_pct列
    city_com = grouped_pct.agg(['mean', 'count'])
    city_com.reset_index(inplace=True)
    city_com['mean'] = round(city_com['mean'], 2)
    data = [(city_com['city'][i], city_com['count'][i])
            for i in range(0, city_com.shape[0])]
    geo = Geo(
        '《西虹市首富》全国热力图',
        title_color="#fff",
        title_pos="center",
        width=1200,
        height=600,
        background_color='#404a59')
    attr, value = geo.cast(data)
    geo.add(
        "",
        attr,
        value,
        type="heatmap",
        visual_range=[0, 200],
        visual_text_color="#fff",
        symbol_size=10,
        is_visualmap=True,
        is_roam=False)
    geo.render('西虹市首富全国热力图.html')


# 爬取数据
# get_tomato_data()
filter_repeat('西虹市首富4.csv', '西虹市首富.xlsx')
# 绘制热力图
# thermodynamic_chart()
