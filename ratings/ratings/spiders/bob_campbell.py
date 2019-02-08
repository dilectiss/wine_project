# -*- coding: utf-8 -*-
# crawler for bob_campbell's ratings
# to scrape the ratings from another expert:
# generate a new spider with the corresponding urls
# all other codes can be reused
import scrapy
from scrapy.http.request import Request

# generated using scrapy's genspider command
class BobCampbellSpider(scrapy.Spider):
    name = 'bob_campbell'
    allowed_domains = ['www.wine-searcher.com']
    start_urls = ['http://www.wine-searcher.com/critics-7-bob+campbell']

# for iterating through the pages of tables
# the number of pages to be scraped can be adjusted by
# changing the value of the range
    def start_requests(self):
    	for i in range(0, 400):
    		yield Request(
    			url='http://www.wine-searcher.com/critics-7-bob+campbell/{0}'.format(i*25+1), 
    			callback=self.parse_table)

# fetch the table data from each page
    def parse_table(self, response):
        for row in response.xpath('//*[@class="nltbl tab-zero"]//tbody/*[@class="wlrwdt"]'):
            yield {
                'wine_name' : row.xpath('td//text()')[2].extract(),
                'vintage': row.xpath('td//text()')[4].extract(),
                'popularity' : row.xpath('td//text()')[5].extract(),
                'score' : row.xpath('td//text()')[8].extract(),
                'avg_price' : row.xpath('td//text()')[11].extract(),
            }
