wine_x
======

.. code:: ipython3

    # -*- coding: utf-8 -*-
    # crawler for the wines table
    #
    # to scrape wines from another critic page:
    # generate a new spider with the corresponding urls
    #
    # For detailed documentation of scrapy functions:
    # https://docs.scrapy.org/en/latest/topics/spiders.html

.. code:: ipython3

    import scrapy
    from scrapy.http.request import Request
    from urllib.parse import urljoin
    from scrapy.spiders import Spider

.. code:: ipython3

    class ProjectSpider(Spider):
      name = 'wine_project'
      rotate_user_agent = True

.. code:: ipython3

    # To craw a critic with initials 'JK':
    #
    # Change the class name 'WineXSpider' to
    # 'WineJKSpider' 
    #
    # Change name = 'wine_x' to 'wine_jk'

.. code:: ipython3

    # Set the start_url to target critic page
    # match the end of url to the starting page

.. code:: ipython3

    class WineXSpider(scrapy.Spider):
        name = 'wine_x'

.. code:: ipython3

        """
        This is the name of the spider used to execute the scrpy crawl function
        """

.. code:: ipython3

        allowed_domains = ['www.wine-searcher.com']

.. code:: ipython3

        """
        This lists the accessible domains for the spider
        """

.. code:: ipython3

        start_urls = ['http://www.wine-searcher.com/critic-x-url/start_page',]

.. code:: ipython3

        """
        The starting url of the spider
        """

.. code:: ipython3

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

.. code:: ipython3

        def start_requests(self):
            for i in range(start,end):

.. code:: ipython3

                """
                Parameters
                ----------
                start: int
                    the desired starting page
                end: int
                    the page after the desired last page
                """

.. code:: ipython3

                yield Request(
                    url='http://www.wine-searcher.com/critic-x-url/{0}'.format((i-1)*25+1),
                    callback=self.parse)

.. code:: ipython3

                """
                The webpage is formatted such that the index {0} is the index of the WINES
                on the particular page. 
                The url here is formatted so that the input page number can be converted
                to yield the desired page. 
                The final index replacing {0} will be (i-1) * 25 + 1, 
                which indicates the index of the first WINE on page i.
                """

.. code:: ipython3

    # This functino traverses through each of the wine pages
    # for the given critic page
    #
    # IMPORTANT: Due to inconsistencies in webpage design
    # 'div[3]' here must change to 'div[1]' for the
    # first page of each critic!

.. code:: ipython3

        def parse(self, response):
            wine = response.xpath('//*[@id="winesortlist"]/div[3]/table/tbody/tr/td[1]/a//@href').extract()

.. code:: ipython3

            """
            This xpath is the location of the RATINGS TABLE on the CRITIC PAGE of the website.
            Each element in the RATINGS TABLE links to the corresponding WINE PAGE.
            The list can then be traversed to allow access to each individual WINE PAGE.
            Due to inconsistencies in webpage design,
            'div[3]' here must be changed to 'div[1]' for the FRIST PAGE of each critic.
            """

.. code:: ipython3

            for w in wine:
                wine_url = urljoin(response.url, w)
                yield scrapy.Request(
                    wine_url, callback=self.parse_wine)

.. code:: ipython3

    # this scrapes the parameters of each wine

.. code:: ipython3

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

.. code:: ipython3

                """
                Inside the WINE PAGE, download the information from the mentioned ten parameters,
                as per the xpath of the html file of each WINE PAGE.
                """
