# -*- coding:utf-8 -*-
#@Time : 2020/4/3 15:11
#@Author : Gva
#@Web : anets.cn
import win_unicode_console
win_unicode_console.enable()
import  os
import  sys
from scrapy import cmdline
from utils.common import getMd5
import json

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# print("哈哈")
print(os.path.dirname(os.path.abspath(__file__)))
cmdline.execute('scrapy crawl crawlOkzyw'.split(' '))

# dsn=[1,2,34]
# json.dumps(dsn,ensure_ascii=False) 

# print(getMd5(''))