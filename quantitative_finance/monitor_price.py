# -*- coding: utf-8 -*-
"""
Created on Sun May 14 11:04:35 2017

@author: xuding
"""
import get_info as a
import sent_email as b

def monitor_price(number_list, flag):        
    for i in range(len(number_list)):
        number       = number_list[i][0]
        remind_price = number_list[i][1]
        orientation  = number_list[i][2]
        
        info, current_price = a.get_info(number)
        
        if  ((current_price > remind_price) and (orientation == 1)):
            if(flag[i] == False):
                b.sent_email(info)
                flag[i] = True
        elif((current_price < remind_price) and (orientation == 0)):
            if(flag[i] == False):
                b.sent_email(info)
                flag[i] = True
