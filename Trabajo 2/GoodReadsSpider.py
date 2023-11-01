import scrapy


class GoodreadsspiderSpider(scrapy.Spider):
    name = "GoodReadsSpider"
    allowed_domains = ["www.goodreads.com"]
    start_urls = ["https://www.goodreads.com/shelf/show/fiction"]

    def parse(self, response):
        pass
