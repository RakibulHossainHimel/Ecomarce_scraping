# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    rating =  scrapy.Field()
    description = scrapy.Field()
    UPC = scrapy.Field()
    Product_type = scrapy.Field()
    Price_excl_tax = scrapy.Field()
    price_incl_tax = scrapy.Field()
    Tax = scrapy.Field()
    Availability = scrapy.Field()
    number_of_review = scrapy.Field()
