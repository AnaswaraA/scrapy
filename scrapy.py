import scrapy
class class ClotheSpider(scrapy.Spider):
    name = 'clothes'
    start_urls = [
        'https://www.carbon38.com/shop-all-activewear/tops',
    ]
    
