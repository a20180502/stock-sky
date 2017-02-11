# coding=utf-8

# 获取所有股票的代码

import urllib2
import re
import os
import sys

from bs4 import BeautifulSoup


import sys
reload(sys)  # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('utf-8')

response = urllib2.urlopen('http://quote.eastmoney.com/stocklist.html')
html = response.read(response)

soup = BeautifulSoup(html, "html.parser", from_encoding="GB18030")

my_list = soup.find_all("li")
# ()中间有代码的项，()需要转义
pattern1 = ".*\(\d+\).*"
pattern2 = ".*>(.*)</a.*"
count = 0
items = {}
for item in my_list:
    item_string = str(item)

    if re.match(pattern1, item_string):
        m = re.match(pattern2, item_string)
        count += 1
        name_code = m.group(1)
        index1 = name_code.index("(")
        index2 = name_code.index(")")
        name = name_code[:index1]
        code = name_code[index1+1:index2]
        items[name] = code
        print name, "->", code
print "Total item is ", count

print "Start to sort items"
new_items = sorted(items.iteritems(), key=lambda d:d[1], reverse = False)
