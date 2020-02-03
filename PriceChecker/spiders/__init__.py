# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
from PriceChecker.items import ProductItem

class AmazonSpider(scrapy.Spider):
    name = "AmazonSpider"

    start_urls= ['https://www.amazon.com/Genuine-Ford-F2UZ-17B883-A-Bumper-Bracket/dp/B000O0K0HO',
        ]

    custom_settings = {'FEED_FORMAT': 'csv',
        'FEED_URI': 'items.csv'
    }
    def parse(self, response):
        product = ProductItem()
        product['ASIN'] = response.xpath('//table[@id="productDetails_detailBullets_sections1"]/tbody/tr[1]/td/@text').extract_first()
        product['Price'] = response.xpath('//span[@id="priceblock_ourprice"]/text()').extract_first()
        print(product)
        yield(product)