import scrapy


class WikispiderSpider(scrapy.Spider):
    name = "WikiSpider"
    allowed_domains = ["es.wikipedia.org"]
    start_urls = ["http://es.wikipedia.org/"]

    def parse(self, response):
        pass
