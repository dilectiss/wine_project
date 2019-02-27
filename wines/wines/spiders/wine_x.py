# -*- coding: utf-8 -*-
# crawler for the wines table
#
# to scrape wines from another critic page:
# generate a new spider with the corresponding urls

import scrapy
from scrapy.http.request import Request
from urllib.parse import urljoin
from scrapy.spider import Spider


class ProjectSpider(Spider):
  name = 'wine_project'
  rotate_user_agent = True

# To craw a critic with initials 'JK':
#
# Change the class name 'WineXSpider' to
# 'WineJKSpider' 
#
# Change name = 'wine_x' to 'wine_jk'
# 
# Set the start_url to target critic page
# match the end of url to the starting page
class WineXSpider(scrapy.Spider):
    name = 'wine_x'
    allowed_domains = ['www.wine-searcher.com']
    start_urls = ['http://www.wine-searcher.com/critic-x-url/start_page',]

# For iterating through the pages of tables
#
# The no. of pages to be scraped is adjusted by
# changing the value of range(includisve, exclusive)
# start: integer; end: integer
#
# Make sure the url is as per the start_url above
# excluding 'start_page'
#
# For efficient scraping, do not set range to be
# above 100 for any one execution
    def start_requests(self):
        for i in range(start,end):
            yield Request(
                url='http://www.wine-searcher.com/critics-1-jancis+robinson/{0}'.format((i-1)*25+1), 
                callback=self.parse)

# This functino traverses through each of the wine pages
# for the given critic page
#
# IMPORTANT: Due to inconsistencies in webpage design
# 'div[3]' here must change to 'div[1]' for the
# first page of each critic!
    def parse(self, response):
        wine = response.xpath('//*[@id="winesortlist"]/div[3]/table/tbody/tr/td[1]/a//@href').extract()
        for w in wine:
            wine_url = urljoin(response.url, w)
            yield scrapy.Request(
                wine_url, callback=self.parse_wine)

# this scrapes the parameters of each wine
    def parse_wine(self, response):
        for row in response.xpath('//*[@id="tab"]/div/div/div[1]/div'):
            yield {
                'name':row.xpath('//*[@id="top_header"]/span[2]//text()').extract(),
                'vintage':row.xpath('//*[@id="top_header"]/span[1]//text()').extract(),
                'avg_price':row.xpath('div[2]/span[2]/b//text()').extract(),
                'producer':row.xpath('div[5]/span[2]/a//text()').extract(),
                'region/appellation':row.xpath('div[6]/span[2]/a[1]//text()').extract(),
                'country':row.xpath('div[6]/span[2]/a//text()')[-1].extract(),
                'blend':row.xpath('div[7]/span[2]/a//text()').extract(),
                'pairing':row.xpath('div[8]/div[2]/span[2]/a//text()').extract(),
                'style':row.xpath('div[9]/div[2]/a//text()').extract(),
                'alcohol':row.xpath('div[10]/div/b//text()').extract(),
            }
     