# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Job(scrapy.Item):
    adWord = scrapy.Field()
    approve = scrapy.Field()
    appShow = scrapy.Field()
    businessZones = scrapy.Field()
    city = scrapy.Field()
    companyFullName = scrapy.Field()
    companyId = scrapy.Field()
    companyLabelList = scrapy.Field()
    companyLogo = scrapy.Field()
    companyShortName = scrapy.Field()
    companySize = scrapy.Field()
    createTime = scrapy.Field()
    deliver = scrapy.Field()
    district = scrapy.Field()
    education = scrapy.Field()
    explain = scrapy.Field()
    financeStage = scrapy.Field()
    firstType = scrapy.Field()
    formatCreateTime = scrapy.Field()
    gradeDescription = scrapy.Field()
    hitags = scrapy.Field()
    imState = scrapy.Field()
    industryField = scrapy.Field()
    industryLables = scrapy.Field()
    isSchoolJob = scrapy.Field()
    jobNature = scrapy.Field()
    lastLogin = scrapy.Field()
    latitude = scrapy.Field()
    linestaion = scrapy.Field()
    longitude = scrapy.Field()
    pcShow = scrapy.Field()
    plus = scrapy.Field()
    positionAdvantage = scrapy.Field()
    positionId = scrapy.Field()
    positionLables = scrapy.Field()
    positionName = scrapy.Field()
    promotionScoreExplain = scrapy.Field()
    publisherId = scrapy.Field()
    resumeProcessDay = scrapy.Field()
    resumeProcessRate = scrapy.Field()
    salary = scrapy.Field()
    score = scrapy.Field()
    secondType = scrapy.Field()
    stationname = scrapy.Field()
    subwayline = scrapy.Field()
    workYear = scrapy.Field()

    xkeyword = scrapy.Field()
    xcrawltime = scrapy.Field()


class Zdm(scrapy.Item):
    _id = scrapy.Field()
    article_id = scrapy.Field()
    article_title = scrapy.Field()
    article_price = scrapy.Field()
    article_url = scrapy.Field()
    article_pic_url = scrapy.Field()
    article_worthy = scrapy.Field()
    article_unworthy = scrapy.Field()
    article_collection = scrapy.Field()
    article_comment = scrapy.Field()

    xcrawltime = scrapy.Field()
