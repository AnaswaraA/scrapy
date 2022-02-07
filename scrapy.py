import scrapy

class CarbonSpider(scrapy.Spider):
    name = "carbons"
    start_urls = [
        "https://carbon38.com/collections/tops/products/miramar-candice-crop"
    ]

      def parse(self, response):
        all_div_quotes = response.css('div.product-detail')
        product_name = response.css(".title ::text").extract_first()
        image_url = response.css("rimage").extract()
        brand = response.css(".vendor ::text")[2].extract()
        price = response.css(".current-price.theme-money::text").get()
        reviews = response.css("okeReviews-reviewsWidget-emptyMessage > p").get()
        breadcrumbs = response.css('.breadcrumbs-list >li.breadcrumbs-list__item >.breadcrumbs-list__link ::text').extract()

        yield {
            'product_name': product_name,
            'image_url': image_url,
            'brand': brand,
            'breadcrumbs': breadcrumbs,
            'price': price,
            'reviews': reviews
        }
    
