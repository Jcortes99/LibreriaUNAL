import scrapy
from scrapy.crawler import CrawlerProcess

class wikiSpider(scrapy.Spider):
    name = 'wiki_spider'
    
    start_urls = ['https://en.wikipedia.org/wiki/YOUR_TOPIC_HERE']

    custom_settings = {
        'ROBOTSTXT_OBEY': True,
        'USER_AGENT': 'YOUR_USER_AGENT',
        'DOWNLOAD_DELAY': 3   # delay between requests
    }

    def parse(self, response):
        print('1')
        # Extract the article's title to construct the filename
        title = response.css('h1::text').get()
        filename = 'C:\\Users\\Usuario\\Documents\\University\\Recuperacion Web\\LibreriaUNAL\\Trabajo 2\\archivos\\'+title.replace(" ", "_") + '.txt'
        
        # Extracting the content
        text = "".join(response.xpath('//p//text()').getall())
        
        # Save the content into a .txt file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(text)
        
        self.log('Saved file %s' % filename)
        # Follow the links to the next pages
        for next_page in response.css('a::attr(href)').getall():
            if next_page is not None and 'wikipedia.org' in next_page:
                next_page_link = response.urljoin(next_page)
                yield scrapy.Request(url=next_page_link, callback=self.parse)