# -*- coding: utf-8 -*-
"""
Created on Sun May 14 14:22:15 2017

@author: xuding
"""

import monitor_price as a
import time

number_list=[['sh600522',10.6,1],
             ['sz002302',22.0,1],
             ['sz000961',7.10,0]]

while(True):
    a.monitor_price(number_list)
    time.sleep(30)