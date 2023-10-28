import scrapy


class Bookspider1Spider(scrapy.Spider):
    name = "BookSpider1"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
      books = response.css('.product_pod')
      for book in books:
        title = book.css('h3 a::attr(title)').get()
        yield { 'title' : title }
