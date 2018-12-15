# -*- coding: utf-8 -*-
# crawler for wines
# to scrape the wines from another critic page:
# generate a new spider with the corresponding urls
# do not modify codes unless specified so
import scrapy
from scrapy.http.request import Request
from urllib.parse import urljoin
from scrapy.spider import Spider


class ProjectSpider(Spider):
  name = 'wine_project'
  rotate_user_agent = True

# Change the class name and 'name' for a
# new spider to crawl a different critic.
# Set the start_url to target critic page
# match the end of url to the starting page.
class WineJRSpider(scrapy.Spider):
    name = 'wine_jr'
    allowed_domains = ['www.wine-searcher.com']
    start_urls = ['http://www.wine-searcher.com/critics-1-jancis+robinson/7501',]

# for iterating through the pages of tables
# The number of pages to be scraped can be adjusted by
# changing the value of the range (includisve, exclusive).
# Make sure the url is as per the start_url
# max range = 2052
    def start_requests(self):
        for i in range(301,601):
            yield Request(
                url='http://www.wine-searcher.com/critics-1-jancis+robinson/{0}'.format((i-1)*25+1), 
                callback=self.parse)

# traversing through each of the wine pages
# NOTE: Due to inconsistencies in webpage design
# 'div[3]' here must change to 'div[1]' for the
# first page of each critic!!!
    def parse(self, response):
        wine = response.xpath('//*[@id="winesortlist"]/div[3]/table/tbody/tr/td[1]/a//@href').extract()
        for w in wine:
            wine_url = urljoin(response.url, w)
            yield scrapy.Request(
                wine_url, callback=self.parse_wine)

# this scrapes the parameters of each wine
    def parse_wine(self, response):
        # if not response.xpath('//*[@id="free-logo"]'):
        #     yield Request(url=response.url, dont_filter=True)
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
     