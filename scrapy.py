import scrapy

class CarbonSpider(scrapy.Spider):
    name = "carbons"
    start_urls = [
        "https://carbon38.com/collections/tops/products/miramar-candice-crop"
    ]

    def parse(self, response):
        all_div_quotes = response.css('div.product-detail')
        product_name = response.css(".title ::text").extract_first()
        brand = response.css(".vendor ::text")[2].extract()
        yield {
            'product_name': product_name,
            'brand': brand
          
        }
    
