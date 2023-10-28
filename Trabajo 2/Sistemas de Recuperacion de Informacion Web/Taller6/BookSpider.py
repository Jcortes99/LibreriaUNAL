import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "BookSpider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
      webpage = response.css('li a')
      for listItem in webpage :
        categoria = listItem.css('::text').get().strip()
        enlace = listItem.css(' ::attr(href)').get()
        yield { 'categoria':categoria , 'url' enlace }
