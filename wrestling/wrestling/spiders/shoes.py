# -*- coding: utf-8 -*-
import scrapy
from wrestling.items import WrestlingItem

class ShoesSpider(scrapy.Spider):
    name = 'shoes'
    allowed_domains = ['eastbay.com']
    start_urls = ['https://www.eastbay.com/Mens/Wrestling/Shoes/_-_/N-1pZ1e8Zne']

    def parse(self, response):
        results = response.xpath("//div[@id='endeca_search_results']//li")
        for result in results:
            item = WrestlingItem()
            item['title'] = results.xpath("a/span[@class='product_title']/text()").extract_first()
            item['price'] = results.xpath("a//span[@class='sale']/text()").extract_first()
            item['img_urls']=results.xpath("//span[@class='product_image']/img/@data-original").extract_first()
            url = results.xpath("a[1]/@href").extract_first()
            yield scrapy.Request(url=url, meta={'item':item}, callback=self.parse_detail, dont_filter=True)
        if len(response.xpath("//a[@class='next']")):
            cte = response.xpath("//a[@class='next']/@href").extract()[0]
            yield scrapy.Request('https://www.eastbay.com'+cte, callback=self.parse)

    def parse_detail(self, response):
        item = response.meta['item']
        item['color'] = response.xpath("//span[@class='attType_color']/text()").extract_first()
        size_list=response.xpath("//span[@id='size_selection_list']/a/text()")
        list = []
        for size in size_list:
            list.append(size)
        item['size'] =list
        item['sku'] = response.xpath("//div[@class='sku_detail']/span/text()").extract_first()
        item['details'] = response.xpath("//div[@id='pdp_description']").xpath("string(.)").extract_first()
        yield item