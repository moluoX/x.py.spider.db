# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
import smtplib
from email.mime.text import MIMEText
from email.header import Header

from spiderdb.dataaccess import get_lagou
from spiderdb.dataaccess import get_zdm


class SpiderDbPipeline(object):
    def process_item(self, item, spider):
        if spider.name == 'lagou':
            db = get_lagou()
            db.position.remove({'positionId': item['positionId']})
            db.position.insert(dict(item))
            return item

        else:
            if item['article_worthy'] < 16:
                return item
            if item['article_unworthy'] > 0 and item['article_worthy'] / item['article_unworthy'] < 4:
                return item

            db = get_zdm()
            exist = db.article.find_one({'_id': item['article_id']})
            if exist:
                if exist['article_worthy'] * 4 > item['article_worthy']:
                    return item
                db.article.remove({'_id': item['article_id']})

            db.article.insert(dict(item))
            self.sendEmail(item, db)
            return item

    def sendEmail(self, item, db):
        keywords = db.keyword.find()
        keymark = ''
        for k in keywords:
            if re.search(k['keyword'], item['article_title']):
                keymark = '♥'
                break
        html = '''<html>
    <body>
        <h1><a href="{1}">[{6}] {0}</a></h1>
        <p><span>值{2} 不{3} 藏{4} 评{5}</span></p>
        <p><image src="{7}" /></p>
    </body>
</html>'''
        mail = MIMEText(
            html.format(item['article_title'], item['article_url'], item['article_worthy'], item['article_unworthy'],
                        item['article_collection'], item['article_comment'], item['article_price'],
                        item['article_pic_url']), 'html', 'utf-8')
        mail['Subject'] = Header('{4}【{0}-{1}】【{2}】{3}'.format(
            item['article_worthy'], item['article_unworthy'], item['article_price'], item['article_title'], keymark),
            'utf-8')
        # mail = MIMEText(html, 'html', 'utf-8')
        # mail['Subject'] = Header('你好', 'utf-8')
        mail['From'] = 'spiderzdm@126.com'
        mail['To'] = '231287196@qq.com'
        mail['Cc'] = 'spiderzdm@126.com'

        smtp = smtplib.SMTP()
        smtp.connect('smtp.126.com', 25)
        smtp.login('spiderzdm', 'spiderzdm11')
        smtp.sendmail('spiderzdm@126.com', ['231287196@qq.com', 'spiderzdm@126.com'], mail.as_string())
        smtp.quit()
