import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ecommerce.items import BookItem

class BookscraperSpider(CrawlSpider):
    name = "bookscraper"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]
    base_url = "https://books.toscrape.com/"
    rules = [Rule(LinkExtractor(restrict_xpaths="//li[@class = 'next' or @class = 'previous']"),
                                callback="parse")]
    
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url,callback=self.parse, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'})
        
    
    custom_settings={
        "AUTOTHROTTLE_ENABKED" : True,
        "DOWNLOAD_DELAY" : 3,
        "CONCURRENT_REQUESTS" : 16
    }




    def parse(self, response):
        headers = response.request.headers
        print(headers)
        for link in response.xpath("//article[@class = 'product_pod']/h3/a/@href"):
            yield response.follow(link, self.product_parse)


    def product_parse(self,response):
        book = BookItem()
        book['title'] = response.xpath("//h1/text()").get()
        book['price'] = response.xpath("//p[@class ='price_color']/text()").get()
        book['rating'] = response.xpath("//p[ contains(@class, 'star-rating')]/@class").get()
        book['description'] = response.xpath("//article[@class = 'product_page']/p/text()").get()
        book['UPC'] = response.xpath("//table//tr[1]/td/text()").get()
        book['Product_type'] = response.xpath("//table//tr[2]/td/text()").get()
        book['Price_excl_tax'] = response.xpath("//table//tr[3]/td/text()").get()
        book['price_incl_tax'] = response.xpath("//table//tr[4]/td/text()").get()
        book['Tax'] = response.xpath("//table//tr[5]/td/text()").get()
        book['Availability'] = response.xpath("//table//tr[6]/td/text()").get()
        book['number_of_review'] = response.xpath("//table//tr[7]/td/text()").get()


        yield book
