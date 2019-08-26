# -*- coding: utf-8 -*-
import scrapy
import requests


class VoteDoctorSpider(scrapy.Spider):
    name = "votedoctor"
    allowed_domains = ["mp.weixin.qq.com"]
    start_urls = ['https://mp.weixin.qq.com/s/b94rn-ycAYfsw7TXHyTWZA']

    def parse(self, response):
        url = 'https://mp.weixin.qq.com/mp/newappmsgvote'
        data = {
            'action': 'vote',
            '__biz': 'MzA4NjkzMDYyOA==',
            'uin': 'MjUyMDAwMjI0Mg==',
            'key': 'd989ddae2a3e4541d49e0c38e5ba49da8f2375d4d0e79e2552b200d2ebb8b6b13ccdfa26ec5ccfdce75b8c35444073381635985abc3d25d6e2478250f602a92c41c6a1b81732eac00c8deee9248d7c1a',
            'pass_ticket': 'x85dkZI0AAW3A1CRq8GiS%2B7KAfmf0AmnM5dxqiEIL3BOvDrYgkB2WYsVvhTSB6d1',
            'appmsg_token': '1023_okY5XSfZ3bX1s9RUT2qX32PDnTEcbAW5AY43mczmoHkO06fuUW_SvhWXKYb3dmZT5GRD_9oHst81e-Cg',
            'f': 'json',
            'json': '{"super_vote_item":[{"vote_id":511952201,"item_idx_list":{"item_idx":["0","1","2","3","4"]}},{"vote_id":511952202,"item_idx_list":{"item_idx":["0","1","2","3","4"]}},{"vote_id":511952203,"item_idx_list":{"item_idx":["0","1","2","3","4"]}}],"super_vote_id":511952200}',
            'idx': '1',
            'mid': '2666519520',
            'wxtoken': '777'
        }
        res = requests.post(url, data=data).content.decode()
        print(res)

