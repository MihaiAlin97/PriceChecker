from PriceChecker.spiders import AmazonSpider
from scrapy.crawler import CrawlerProcess

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(AmazonSpider)
    process.start()