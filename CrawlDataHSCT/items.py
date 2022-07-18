# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class CrawldatahsctItem(Item):
    company_name = Field()
    company_code = Field()
