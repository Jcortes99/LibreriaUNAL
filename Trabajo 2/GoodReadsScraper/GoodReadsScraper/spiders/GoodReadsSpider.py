import scrapy
from bs4 import BeautifulSoup

class GoodReadsSpider(scrapy.Spider):
    # Name of our spider bot
    name = 'goodreads'
    
    # Initial URLs to visit
    start_urls = ['https://www.goodreads.com/shelf/show/young-adult']

    aux = 0
    
    id = 1447
    
    def autoId(self):
        self.id += 1
        return str(self.id)

    def parse(self, response):
        # Selector for book items
        for book in response.css('.bookTitle::attr(href)'):
            url = book.get()
            self.aux += 1
            if url is not None:
                yield response.follow(url, self.parse_book)

        # Select the NEXT button link and parse pages recursively
        # if self.aux < 10:
        next_page = response.css('div.pagination a.next_page::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def parse_book(self, response):
        title = response.css('h1.Text.Text__title1::text').get().strip()
        
        span_html = response.css('.Formatted').get()
        soup = BeautifulSoup(span_html, 'html.parser')
        synopsis = ''.join(soup.stripped_strings)
        
        path = '../../../archivos//'+ self.autoId() + '.txt'
        
        with open(path, 'w') as f:
            f.write(f'{title}\n{synopsis}')