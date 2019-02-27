# -*- coding: utf-8 -*-
# crawler for the wines table
#
# to scrape wines from another critic page:
# generate a new spider with the corresponding urls
#
# For detailed documentation of scrapy functions:
# https://docs.scrapy.org/en/latest/topics/spiders.html

import scrapy
from scrapy.http.request import Request
from urllib.parse import urljoin
from scrapy.spider import Spider


class ProjectSpider(Spider):
  name = 'wine_project'
  """
  This class represents the wine_project class for scraping wine data
  """
  rotate_user_agent = True
  """
  This is for rotating the user_agent as per the settings.py file
  """

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
    """
    This is the name of the spider used to execute the scrpy crawl function
    """
    allowed_domains = ['www.wine-searcher.com']
    """
    This lists the accessible domains for the spider
    """
    start_urls = ['http://www.wine-searcher.com/critic-x-url/start_page',]
    """
    The starting url of the spider
    """

# For iterating through the pages of tables
#
# The no. of pages to be scraped is adjusted by
# changing the value of range(includisve, exclusive)
#
# Replace the url as per the start_url above
# excluding 'start_page', which is here a dynamic index {0}
#
# For efficient scraping, do not set range to be
# above 100 for any one execution
    def start_requests(self):
        for i in range(start,end):
            """
            Parameters
            ----------
            start: int
                the desired starting page
            end: int
                the page after the desired last page
            """
            yield Request(
                url='http://www.wine-searcher.com/critic-x-url/{0}'.format((i-1)*25+1),
                callback=self.parse)
            """
            The webpage is formatted such that the index {0} is the index of the WINES
            on the particular page. 
            The url here is formatted so that the input page number can be converted
            to yield the desired page. 
            The final index replacing {0} will be (i-1) * 25 + 1, 
            which indicates the index of the first WINE on page i.
            """

# This functino traverses through each of the WINE PAGES
# for the given CRITIC PAGE
#
# IMPORTANT: Due to inconsistencies in webpage design
# 'div[3]' here must change to 'div[1]' for the
# first page of each critic!
    def parse(self, response):
        """
        parse processes download responses.

        Parameters
        ----------
        self: url
            current url, as yielded by the previous function start_requests
        response: the response to parse
        """
        wine = response.xpath('//*[@id="winesortlist"]/div[3]/table/tbody/tr/td[1]/a//@href').extract()
        """
        Extract the PATH of the WINE PAGE.
        This xpath is the location of the RATINGS TABLE on the CRITIC PAGE of the website.
        Each element in the RATINGS TABLE links to the corresponding WINE PAGE via
        the PATH of the WINE PAGE
        The list can then be traversed to allow access to each individual WINE PAGE.
        Due to inconsistencies in webpage design,
        'div[3]' here must be changed to 'div[1]' for the FRIST PAGE of each critic.
        """
        for w in wine:
            wine_url = urljoin(response.url, w)
            """
            Parameters
            ----------
            w: path
                PATH of the WINE PAGE
            wine_url is the new url created by replacing the path of the base url
            from the CRITICS PAGE with the path of the WINE PAGE 
            """
            yield scrapy.Request(
                wine_url, callback=self.parse_wine)
            """
            Ths function is for calling on the resulting WINE PAGE url.
            """

# this scrapes the parameters of each wine
    def parse_wine(self, response):
        """
        parse_wine functions like parse, except this time the url 
        self that is called upon is the WINE PAGE
        """
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
            """
            Inside the WINE PAGE, download the information from the mentioned ten parameters,
            as per the xpath of the html file of each WINE PAGE.
            """
     