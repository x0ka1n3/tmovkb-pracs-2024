import scrapy

class ildarSpider(scrapy.Spider):
    name = 'ildar_spider'
    start_urls = ['https://wishmaster.me/catalog/smartfony/']

    def parse(self, response):
        for phone in response.css('div.product-item'):
            yield {
                'title': " ".join([i for i in phone.css('div.product-item-title').css('a::text').get().replace("\n","").split(" ") if i!=""]),
                # 'author': quote.css('span small::text').get(),
                # 'tags': quote.css('div.tags a.tag::text').getall(),
                "price": " ".join([i for i in phone.css("div.product-item-price-current__price").css("span.product-item-price-current::text").get().replace("\n","").replace(r"\xa","").split(" ") if i != ""])
            }

        # yield from response.follow_all(css='li.next a', callback=self.parse)
