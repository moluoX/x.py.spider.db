import smtplib
from email.header import Header
from email.mime.text import MIMEText


mail = MIMEText('你好', 'html', 'utf-8')
mail['Subject'] = Header('你好', 'utf-8')
mail['From'] = 'spiderzdm@126.com'
mail['To'] = '231287196@qq.com'
mail['Cc'] = 'spiderzdm@126.com'

smtp = smtplib.SMTP()
smtp.connect('smtp.126.com', 25)
smtp.login('spiderzdm', 'spiderzdm11')
smtp.sendmail('spiderzdm@126.com', ['231287196@qq.com', 'spiderzdm@126.com'], mail.as_string())
smtp.quit()

print('已发送')
