import scrapy
class class ClotheSpider(scrapy.Spider):
    name = 'clothes'
    start_urls = [
        'https://www.carbon38.com/shop-all-activewear/tops',
    ]
    
    def parse(self, response):
        print(response.css("div.product-block").get())

    
