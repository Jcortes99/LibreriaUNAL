import scrapy


class Bookspider3Spider(scrapy.Spider):
    name = "BookSpider3"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
      books = response.css('.product_pod')
      for book in books:
        title = book.css('h3 a::attr(title)').get()
        price = book.css('div p::text').get().strip()
        url = book.css('h3 a::attr(href)').get()
        yield { 'title' : title , 'price' : price, 'url' : url }
      next_page = response.css('li.next a::attr(href)').get()
      if next_page is not None:
        yield response.follow(next_page, callback=self.parse)
