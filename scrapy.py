import scrapy

class CarbonSpider(scrapy.Spider):
    name = "carbons"
    start_urls = [
        "https://carbon38.com/collections/tops/products/miramar-candice-crop"
    ]

    def parse(self, response):
        all_div_quotes = response.css('div.product-detail')
        product_name = response.css(".title-row").extract_first()
        yield {
            'product_name': product_name
          
        }
    
