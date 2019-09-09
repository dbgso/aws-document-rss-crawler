# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response.text import TextResponse, Response
from scrapy_splash import SplashRequest

class AmzondocsSpider(scrapy.Spider):
    name = 'amzondocs'
    allowed_domains = []
    start_urls = ['https://docs.aws.amazon.com']

    def start_requests(self):
        for i in self.start_urls:
            yield SplashRequest(i, self.parse,
                args={'wait': 2},
            )

    def parse(self, response: Response):
        # print(response.url, len(response.css('.awsui-cards-container .awsui-cards-card-header a')))
        if 'https://docs.aws.amazon.com' == response.url:
            for href in response.css('.awsui-cards-card-container a::attr(href)').extract():
                nextHref = response.urljoin(href)
                # print(nextHref)
                if not  '?id' in href:
                    continue
                # print(nextHref)
                yield SplashRequest(nextHref, self.nparse,
                    args={'wait': 2},
                )

    def nparse(self, response: Response):
        for href in response.css('.awsui-cards-container .awsui-cards-card-header a::attr(href)').extract():
            if '.html' not in href:
                continue
            nextHref = response.urljoin(href)
            yield scrapy.Request(nextHref, self.aparse)

    def aparse(self, response: Response):
        if '.html' in response.url:
            hreflist = response.css('a.btn-rss-link::attr(href)').extract()
            for href in hreflist:
                link = response.urljoin(href)
                yield {"link": link}
