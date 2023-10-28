import scrapy


class BookSpider(scrapy.Spider):
    name = 'bookspider'
    start_urls = ['https://books.toscrape.com']

    def parse(self, response):
        # buscar todos los enlaces a libros
        for book_url in response.css('article.product_pod h3 a::attr(href)').getall():
            yield response.follow(book_url, self.parse_book_info)

        # continuar con la siguiente página si la hay
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def parse_book_info(self, response):
        book_info = {
            'Nombre': response.css('div.product_main h1::text').get(),
            'url': response.url,
            'Precio': response.css('p.price_color::text').get(),
            'Impuesto': response.css('table.table.table-striped tr:nth-child(5) td::text').get(),
            'Tipo_Producto': response.css('table.table.table-striped tr:nth-child(2) td::text').get(),
            'Disponibilidad': response.css('p.instock.availability::text').get().strip(),
            'calificacion': self.get_book_rating(response),
            'Reseñas': response.css('div#comments div.comment p::text').getall()
        }
        yield book_info

    @staticmethod
    def get_book_rating(response):
        rating = response.css('div.product_main p.star-rating::attr(class)').get().replace('star-rating', '').strip()
        rating_dict = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
        return rating_dict.get(rating, 'N/A')