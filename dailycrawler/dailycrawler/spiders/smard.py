import scrapy
from scrapy_splash import SplashRequest, SplashFormRequest

from scrapy.http import FormRequest
# from urllib.parse import urlparse
from scrapy.utils.response import open_in_browser


class SmardSpider(scrapy.Spider):
    name = 'smard'
    # allowed_domains = ['www.smard.de/en/']
    start_urls = ['https://www.smard.de/en/']

    def parse(self, response):
        homepage = 'https://www.smard.de'
        link = response.xpath("//a[contains(text(), ' Data download')]/@href").get()
        downloadspage = homepage+link

        # print(f'{downloadspage}')
        downloadAttributes= {
            "selectedCategory"    :'2',
            "selectedSubCategory" :'3',
            "selectedRegion"      :"DE",
            "from"                :'1590962400000',
            "to"                  :'1596232799999',
            "selectedFileType"    :"CSV"
            }
        
        test_link = 'https://www.smard.de/en/downloadcenter/download_market_data/5730#!?downloadAttributes={"selectedCategory":1,"selectedSubCategory":2,"selectedRegion":"DE","from":1590962400000,"to":1596232799999,"selectedFileType":"CSV"}'

        # yield SplashFormRequest(url=downloadspage, formdata = downloadAttributes, callback=self.downloadspage)
        yield SplashRequest(url=test_link, callback=self.downloadspage, endpoint='render.html')

    def downloadspage(self, response):
        # response.xpath(//button[@type="button" and @name="button" and contains(text(), "Download file" )])
        # open_in_browser(response)

        local button = splash:select('button')
        button:mouse_click()

        # pass



# 1 Electricity generation   ->  1. Actual 2. Forecasted 3. Installed
# 2 Electricity consumption  ->  5. Actual  6. Forecasted
# 3 Market          ->  31. Cross-border physical  22. Scheduled commercial  8. Day-Ahead Prices
# 5 Balancing       ->  19. Teriti 20. Exported bala 17.primary Control 18.secondar control
#                       21. imported balancing 16. total costs 15. balancing energy
