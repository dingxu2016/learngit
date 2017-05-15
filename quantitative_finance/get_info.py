# -*- coding: utf-8 -*-
"""
Created on Sat May 13 23:12:00 2017

@author: xuding
"""

import urllib.request

def get_info(num):
    #获取新浪财经接口提供的数据
    url = 'http://hq.sinajs.cn/?list=%s' % num
    req = urllib.request.Request(url)
    content = urllib.request.urlopen(req).read()
    
    #提取所要使用的数据
    str  = content.decode('gbk')
    data = str.split('"')[1].split(',')
    name = "%-6s" %data[0]
    
    current_price  = "%-6s" % (float(data[3]))
    change_price   = "%-6s" % round(float(data[3]) - float(data[2]), 2)
    change_percent = (float(data[3]) - float(data[2])) * 100 / float(data[2])
    change_percent = "%-2s" %round(change_percent,2)
    change_percent += '%'
   
    #返回所需要的数据
    info = "股票名字:{0}涨跌价:{1}涨跌幅:{2}  最新价:{3}".format(name, change_price, change_percent, current_price)
    return (info, float(current_price))