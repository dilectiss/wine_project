# wine-project
wine-project CVBE: wine ratings and big data

Spiders for crawling wine data

Instructions for wine crawler:

INSTALL:
python 3.7 (follow instructions on installing conda here: http://docs.anaconda.com/anaconda-cloud/user-guide/getting-started/#finding-downloading-and-installing-packages)
scrapy (https://scrapy.org)
scrapy-rotating-proxies:
    pip install scrapy-rotating-proxies

USE OF SPIDER:
Files to check and modify:
In wines/spiders/
    wine_robert_parker.py
    Change the name of this file in accord with the wine_critic page you're crawling
    Instructions for modifying the file are infile
In wines/
    settings.py

Settings parameters to modify
IMPORTANT: Please use a new list of EU-currency IP for ROTATING_PROXY_LIST.
Please update ROTATING_PROXY_PAGE_RETRY_TIMES = number of IP in the list.
Scraping etiquette:
DO NOT descrease DOWNLOAD_DELAY to below 5
DO NOT increase CONCURRENT_REQUESTS to above 1
    in the case of timeout or loops with IP addresses:
        1. get rid of DOWNLOAD_TIMEOUT and DNS_TIMEOUT
    in the case of IP ban (confirmed by trying to visit the website in a browser):
        1. use a fresh and large set of proxies
        
Use a VPN before crawling to avoid IP.

COMMAND FOR CRAWLING:
    scrapy crawl <spider name> -o file.csv -t csv
    this will output a csv file in the folder of your current command location
    please make a copy of the folders here and crawl in the local folder of the spider
    modify <spider name> to wine_robert_parker (for example, or whichever spider name you have modified the spider to)
    modify file.csv to desired file name
