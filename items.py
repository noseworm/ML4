# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Property(scrapy.Item):
	data_code = scrapy.Field()
	latitude = scrapy.Field()
	longtitude = scrapy.Field()
	property_type = scrapy.Field()
	address = scrapy.Field()
	city = scrapy.Field()
	askprice = scrapy.Field()
	sellingprice = scrapy.Field()
	year_built = scrapy.Field()
	living_area = scrapy.Field()
	num_parking = scrapy.Field()
	num_bath = scrapy.Field()
	num_bed = scrapy.Field()
	num_room = scrapy.Field()
	sold_date = scrapy.Field()