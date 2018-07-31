#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pyecharts import Style
from pyecharts import Geo

# 读取城市数据
city = []

with open('filter_movie.txt', 'r', encoding='utf-8') as f:
    rows = f.readlines()
    for row in rows:
        if len(row.split(',')) == 5:
            city.append(row.split(',')[2].replace('\n', ''))


def all_list(arr):
    result = {}
    for i in set(arr):
        result[i] = arr.count(i)
    return result


data = []
for item in all_list(city):
    data.append((item, all_list(city)[item]))
    style = Style(
        title_color="#fff",
        title_pos="center",
        width=1200,
        height=600,
        background_color="#404a59")

geo = Geo("《邪不压正》粉丝人群地理位置", "数据来源：恋习Python", **style.init_style)

# geo.add_coordinate('灯塔', 123.33, 41.42)
# geo.add_coordinate('方城', 113.0, 33.27)
# geo.add_coordinate('桃源', 111.48, 28.9)
# geo.add_coordinate('高陵', 109.08, 34.53)
# geo.add_coordinate('徐闻', 110.17, 20.33)

f = open('data.txt', 'w', encoding='utf-8')
for item in data:
    f.writelines(str(item) + '\n')
f.close()
attr, value = geo.cast(data)

geo.add(
    "",
    attr,
    value,
    visual_range=[0, 20],
    visual_text_color="#fff",
    symbol_size=20,
    is_visualmap=True,
    is_piecewise=True,
    visual_split_number=4)

geo.render("邪不压正.html")
