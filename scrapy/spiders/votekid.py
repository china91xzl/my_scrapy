# -*- coding: utf-8 -*-
import scrapy
import requests
import re


class VoteKidSpider(scrapy.Spider):
    name = "votekid"
    # redis_key = 'start_urls'

    allowed_domains = ["vote.syhpvip.com"]
    start_urls = ['http://vote.syhpvip.com/']

    def parse(self, response):
        # city_names = response.xpath('//h3[@class="city-name"]/text()').extract()
        # print(response.body.decode())
        times = 100
        dataa = {
            'userInfoId': ''}
        url = 'http://vote.syhpvip.com'
        url_a = 'http://vote.syhpvip.com/userInfo/add'
        url_p = 'http://vote.syhpvip.com/voteRecords/add'
        # requests.get(url)
        findu = 'http://vote.syhpvip.com/opusInfo/getVoteRanking'
        dataf = {
            'current': '1',
            'size': '20',
            'count': '1030',
            'areaId': '360100',
            'opusGroup': '小话筒视频中班组'
        }
        i = 0
        while i < times:
            resa = requests.post(url_a, data=dataa).content.decode()
            user_id = re.findall('"userInfoId":"(.*?)"', resa)[0]
            datap = {
                'opusInfoId': '296',
                'userInfoId': user_id
            }
            j = 0
            while j < 3:
                resp = requests.post(url_p, data=datap).content.decode()
                j = j + 1
                i = i + 1
            resf = requests.post(findu, data=dataf).content.decode()
            num = re.findall('"过火焰山",(.*?)areaName', resf, re.S | re.M)[0]
            vots = re.findall('"votes":(.*?)\\n', num, re.S | re.M)[0]
            print('投票成功，当前票数：'+vots)

        # item = FlightInfoItem()
        # for city_name in city_names:
        #     item = FlightInfoItem()
        #     item['city'] = '深圳'
        # item['city'] = '宿务'
        # item['price'] = '800'
        # item['date'] = '2019-09-09'
        # yield item
