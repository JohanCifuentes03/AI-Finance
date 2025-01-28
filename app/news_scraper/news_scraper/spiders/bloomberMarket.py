import scrapy


class BloombermarketSpider(scrapy.Spider):
    name = "bloomberMarket"
    allowed_domains = ["bloomberg.com"]
    start_urls = ["https://www.bloomberg.com/markets"]

    def parse(self, response):
        pass
