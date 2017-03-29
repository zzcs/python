#!/usr/bin/Python3
# -*- coding: utf-8 -*-

import urllib.request
from urllib import parse
from bs4 import BeautifulSoup
import re

url = "https://en.wikipedia.org/wiki/Mobile_country_code";
get = urllib.request.urlopen(url).read();
soup = BeautifulSoup(get,"html.parser");#解析html文档
location = soup.find_all(id="siteSub");#获取信息的网站
location_name = location[0].string;
title = soup.h1.string;#mobile country code
#得到每个洲的洲名	
country_prefix = soup.find_all(href= re.compile("/wiki/List_of_mobile_network_operators_of_"));
Area = [];
Area = list();
for country in country_prefix:
	Area.append(country.string);
print(Area);
#print(soup.h1.string);#得到这个tag的文字