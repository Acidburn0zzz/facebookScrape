import scrapy
import json

# import logging
# from scrapy.utils.log import configure_logging

cookies = open('./cookies.json')
dictCookies = json.load(cookies)

# configure_logging(install_root_handler=False)
# logging.basicConfig(
#     filename='log.txt',
#     format='%(levelname)s: %(message)s',
#     level=logging.INFO
# )


class FbSpyder(scrapy.Spider):
    name = "fbScrape",
    USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.97 Safari/537.22 AlexaToolbar/alxg-3.1"

    def start_requests(self):
        urls = [
            'http://www.facebook.com'
        ]
        for url in urls:
            yield scrapy.Request(url=url, cookies=dictCookies, callback=self.parse)

    def parse(self, response):
        with open('log.html', 'a') as f:
            print(response.body, file=f)
