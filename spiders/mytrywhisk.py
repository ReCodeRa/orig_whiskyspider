import scrapy


class MytrywhiskSpider(scrapy.Spider):
    name = 'mytrywhisk'
    allowed_domains = ['www.whiskyshop.com']
    start_urls = ['http://www.whiskyshop.com/']

    def parse(self, response):
        for item in response.css('.product-item-info'):
            res = []
            yield r = {
                'brand' : item.css('.product-item-link::text').get()
                'link' : item.css('.product-item-link::attr(href)').get()
                'price' : item.css('.price::text').get()
            }
            res.append(r)
        
        next_page = response.css('.action.next::attr[href]')
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)