#!/usr/bin/python3
# coding: utf-8
from django.core.mail import send_mail as dj_send_mail

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

def send_mail(title, message, receivers):
    print('-----开始发送邮件----')
    dj_send_mail(title, '',
                 html_message=message,
                 from_email='disenQF@163.com',
                 recipient_list=receivers)

    print('--发送完成!-')


def send_message(title, message, receivers):
    client = smtplib.SMTP('smtp.163.com',port=25)
    client.debuglevel = 1

    client.login('disenQF@163.com', 'xapython1903')

    # message = '<html><h3>亲爱的Disen:</h3><p>您注册的用户需要<a href="http://localhost:8080/">激活</a>才能正常使用</p></html>'
    # title = '易果平台-用户激活通知'

    # 第二个参数是内容的类型， html 富文本， plain 文本
    message = MIMEText(message, 'html', 'utf-8')
    message['Subject'] = Header(title, 'utf-8')
    message['From'] = 'disenQF@163.com'
    message['To'] = ','.join(receivers)

    client.send_message(message,
                        from_addr='disenQF@163.com',
                        to_addrs=receivers)

    print('---ok--')


if __name__ == '__main__':
    message = '<html><h3>亲爱的Disen:</h3><p>您注册的用户需要<a href="http://localhost:8080/">激活</a>才能正常使用</p></html>'
    title = '易果平台-用户激活通知'
    send_message(title, message, ['610039018@qq.com'])
