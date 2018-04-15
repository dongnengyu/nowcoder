# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import DmozItem


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]

    start_urls = [
        "https://www.nowcoder.com/ta/review-java/review?page=120",
    ]


    i = 119;
    while i:
        start_urls.append("https://www.nowcoder.com/ta/review-java/review?page="+str(i))
        i=i-1

    def parse(self, response):
        for href in response.css("ul.directory.dir-col > li > a::attr('href')"):
            url = response.urljoin(response.url, href.extract())
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse(self, response):
        for sel in response.xpath('/html/*'):
            item = DmozItem()
            item['title'] = sel.xpath('normalize-space(//div[@class="final-question"]/text())').extract()
            item['answer'] = sel.xpath('normalize-space(//div[@class="design-answer-box"])').extract()
            #item['desc'] = sel.xpath('text()').extract()
            yield item
