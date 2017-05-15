# -*- coding: utf-8 -*-
"""
Created on Sat May 13 22:42:32 2017

@author: xuding
"""

import smtplib
from email.mime.text import MIMEText
from email.header    import Header
from email.utils     import parseaddr, formataddr


def sent_email(s):
    #email setting ----------------------------
    my_sender = 'xudingflame@163.com'
    my_pass   = '13308011530XD'
    receiver  = ['315280790@qq.com']
    #email setting ----------------------------
    
    #email content ----------------------------
    msg            = MIMEText(s, 'plain', 'utf-8')
    msg['From']    = _format_addr("鼎哥哥 <%s>" % my_sender)
    msg['To']      = _format_addr("小股神 <%s>" % receiver)
    msg['Subject'] = Header('股票实时数据', 'utf-8').encode()
    #email content ----------------------------
    
    try:
        smtpObj = smtplib.SMTP('smtp.163.com', 25)
        smtpObj.login(my_sender, my_pass)
        smtpObj.sendmail(my_sender, receiver, msg.as_string())
        smtpObj.quit()
        print("邮件发送成功")
    except:
        print("Error:无法发送邮件")

def _format_addr(a):
    name, addr = parseaddr(a)
    return formataddr((Header(name, 'utf-8').encode(), addr))