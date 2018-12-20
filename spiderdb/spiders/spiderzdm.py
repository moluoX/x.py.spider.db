import uuid
from datetime import datetime

import scrapy
import json

from spiderdb.items import Zdm


class SpiderZdm(scrapy.spiders.CrawlSpider):
    baseUrl = 'https://www.smzdm.com/jingxuan/json_more?filter=s0f0t0b0d0r0p{0}'
    headers = {'Referer': 'https://www.smzdm.com/jingxuan'}

    name = 'zdm'
    allowed_domains = ['smzdm.com']

    # custom_settings = {
    #     'DEFAULT_REQUEST_HEADERS': headers
    # }

    def start_requests(self):
        return [scrapy.Request(SpiderZdm.baseUrl.format(1), callback=self.parse,
                               meta={'page': 1}, headers=SpiderZdm.headers,
                               cookies={'JSESSIONID': str(uuid.uuid4()), 'user_trace_token': str(uuid.uuid4())})]

    def parse(self, response):
        page = response.meta['page']

        if response.status == 200:
            body = response.body.decode('utf-8')
            res = json.loads(body)

            for x in res['article_list']:
                m = Zdm()
                m['xcrawltime'] = datetime.now()
                m['_id'] = x['article_id']
                m['article_id'] = x['article_id']
                m['article_title'] = x['article_title']
                m['article_price'] = x['article_price']
                m['article_url'] = x['article_url']
                m['article_pic_url'] = x['article_pic_url']
                m['article_worthy'] = int(x['article_worthy'])
                m['article_unworthy'] = int(x['article_unworthy'])
                m['article_collection'] = int(x['article_collection'])
                m['article_comment'] = int(x['article_comment'])
                yield m

            page += 1
            if page > 100:
                page = 1

        yield scrapy.Request(SpiderZdm.baseUrl.format(page), callback=self.parse,
                             meta={'page': page}, headers=SpiderZdm.headers,
                             cookies={'JSESSIONID': str(uuid.uuid4()), 'user_trace_token': str(uuid.uuid4())})
