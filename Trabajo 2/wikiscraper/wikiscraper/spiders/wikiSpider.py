import scrapy
from scrapy.crawler import CrawlerProcess

class WikiSpider(scrapy.Spider):
    name = 'wiki_spider'
    
    start_urls = ['https://es.wikipedia.org/wiki/Programaci%C3%B3n']

    custom_settings = {
        'ROBOTSTXT_OBEY': True,
        'USER_AGENT': 'YOUR_USER_AGENT',
        'DOWNLOAD_DELAY': 3   # delay between requests
    }

    def autoId(self):
        self.idcount += 1
        return str(self.idcount)

    def parse(self, response):
        
        # Verify the limit hasn't been exceeded yet
        if self.articles_crawled >= self.MAX_ARTICLES:
            return

        # Increase the number of crawled pages
        self.articles_crawled += 1
        
        # Extract the article's title to construct the filename
        title = response.css('h1::text').get()
        filename = 'C:\\Users\\Usuario\\Documents\\University\\Recuperacion Web\\LibreriaUNAL\\Trabajo 2\\archivos\\'+ self.autoId() + '.txt'
        
        # Extracting the content
        text = "".join(response.xpath('//p//text()').getall())
        
        # Save the content into a .txt file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(text)
        
        self.log('Saved file %s' % filename)
        # Follow the links to the next pages
        links = response.css('a')
        self.log('Found %d links' % len(links))

        for next_page in links:
            href = next_page.xpath('@href').get()
            class_name = next_page.xpath('@class').get()
            if 'interlanguage-link' not in class_name: 
                if href is not None and 'wikipedia.org' in href:
                    next_page_link = response.urljoin(href)
                    yield scrapy.Request(url=next_page_link, callback=self.parse)