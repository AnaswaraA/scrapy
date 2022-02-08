
import collections
import scrapy
from ..items import ClotheItem

class CarbonSpider(scrapy.Spider):
    name = "carbons"
    start_urls = [
        "https://www.carbon38.com/shop-all-activewear/tops"
    ]
    page_number = 2
    count = 1

    scraped_count = collections.defaultdict(int)
    limit = 100

    def parse(self, response):
        for link in response.css(".image-cont a::attr(href)"):
            yield response.follow(link.get(), callback=self.parse_products)

    def parse_products(self, response):
        items = ClotheItem()
        product_name = response.css(".title ::text").extract_first()
        image_url = response.css("img.rimage__image ::attr(src)").get()
        brand = response.css(".vendor ::text")[2].extract()
        price = response.css(".current-price.theme-money::text").get()
        reviews = response.css(".container>.okeReviews >.okeReviews-reviewsWidget-emptyMessage>.p").extract()
        breadcrumbs = response.css('.breadcrumbs-list >li.breadcrumbs-list__item >.breadcrumbs-list__link ::text').extract()
        colour = response.css('.selector-wrapper ::text ')[4].extract()
        description = response.css('details.cc-accordion-item >.cc-accordion-item__panel ::text')[1].extract()
        sku = response.xpath('string(//body)').re(r"sku: (^\W\d-$)")
        # sku = response.css("details.cc-accordion-item >.cc-accordion-item__panel >.cc-accordion-item__content ::text")[6].extract()
        product_id = response.xpath('string(//body)').re(r"product_id: (\d+)")
        sizes = response.css('#SingleOptionSelector-1 option ::text').getall()
        items['breadcrumbs'] = breadcrumbs
        items['image_url'] = image_url
        items['brand'] = brand
        items['product_name'] = product_name
        items['price'] = price
        items['reviews'] = reviews
        items['colour'] = colour
        items['sizes'] = sizes
        items['description'] = description
        items['sku'] = sku
        items['product_id'] = product_id
        yield items

        next_page = 'https://carbon38.com/collections/tops?page='+ str(CarbonSpider.page_number)
        if CarbonSpider.page_number < 4:
            yield response.follow(next_page, callback = self.parse)
            

    
