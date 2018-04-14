# -*- coding: utf-8 -*-
import scrapy


class JdbookSpider(scrapy.Spider):
    name = "jdbook"
    allowed_domains = ["jd.com"]
    start_urls = (
        'http://www.jd.com/',
    )

    def parse(self, response):
        pass
