
import uuid
from datetime import datetime
from urllib.parse import quote

import scrapy
import json

from spiderdb.dataaccess import get_lagou
from spiderdb.items import Job


class SpiderLG(scrapy.spiders.CrawlSpider):
    baseUrl = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&kd={0}&pn={1}'
    headers = {'Referer': 'https://www.lagou.com/jobs/list_'}

    name = 'lagou'
    allowed_domains = ['lagou.com']

    # custom_settings = {
    #     'DEFAULT_REQUEST_HEADERS': headers
    # }

    def start_requests(self):
        db = get_lagou()
        keywords = db.keyword.find()
        return [scrapy.Request(SpiderLG.baseUrl.format(quote(keyword['keyword']), 1), callback=self.parse,
                               meta={'keyword': keyword['keyword'], 'page': 1}, headers=SpiderLG.headers,
                               cookies={'JSESSIONID': str(uuid.uuid4()), 'user_trace_token': str(uuid.uuid4())})
                for keyword in keywords]

    def parse(self, response):
        page = response.meta['page']

        if response.status == 200:
            body = response.body.decode('utf-8')
            res = json.loads(body)
            if res['success']:
                if len(res['content']['positionResult']['result']) == 0:
                    print('已完成全部数据抓取:{0}'.format(response.meta['keyword']))
                    return []

                for x in res['content']['positionResult']['result']:
                    m = Job(x)
                    m['xkeyword'] = response.meta['keyword']
                    m['xcrawltime'] = datetime.now()
                    yield m

                page += 1

        yield scrapy.Request(SpiderLG.baseUrl.format(quote(response.meta['keyword']), page), callback=self.parse,
                             meta={'keyword': response.meta['keyword'], 'page': page}, headers=SpiderLG.headers,
                             cookies={'JSESSIONID': str(uuid.uuid4()), 'user_trace_token': str(uuid.uuid4())})
