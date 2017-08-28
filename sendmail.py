#coding=utf-8

from email.mime.text import MIMEText
from email.mime.multipart import    MIMEMultipart
import smtplib,time

class Sendmail():
    def send(self,filename):
        msg = MIMEMultipart()

        timestr = time.strftime('%y%m%d%H%M%S', time.localtime())
        thebody = MIMEText(u'乐享付自动化测试结果'+timestr, 'plain', 'utf-8')
        msg.attach(thebody)

        att = MIMEText(open(filename, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="result_report.html"'
        msg.attach(att)

        msg['to'] = 'chenzhiqun@yazuo.com;quhongbo@yazuo.com;liuchongsong@yazuo.com'
        msg['from'] = 'chenzhiqun@yazuo.com'
        msg['subject'] = u'自动化测试报告'
        try:
            server=smtplib.SMTP()
            server.connect('mail.yazuo.com')
            server.login('chenzhiqun@yazuo.com','czqyazuo1234')
            server.sendmail(msg['from'],msg['to'].split(';'),msg.as_string())
            server.quit()
            print '发送成功'
        except Exception, e:
            print str(e)

            #if __name__=='__main__':

            #   mail=Sendmail()

            #  mail.send('E:\\android\\result_report.html')