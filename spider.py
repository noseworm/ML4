import scrapy
from tutorial.items import Property
from scrapy.http import Request
import functools

def cleanprice(str):
	str = str[0]
	str = str.replace("\\xa", "")
	return str.replace("$","")

def convertSqInch(met):
	return met*1550.0031

class DuPropSpider(scrapy.Spider):
	name = "DuProp"
	allowed_domains = ["duproprio.com"]
	start_url = "http://duproprio.com/search/?hash=/g-re=6/s-pmin=0/s-pmax=99999999/s-build=1/s-days=0/s-filter=forsale/p-con=main/p-ord=date/p-dir=DESC/pa-ge=%s/"
	def parse(self, response):
		for sel in response.xpath('//ol[@id="searchResults"]/*'):
			item = Property()		
			item["data_code"] = sel.xpath('@data-code').extract()
			if(len(item["data_code"]) == 0):
				continue
			item["latitude"] = sel.xpath('div[@itemprop="contentLocation"]/div[@itemprop="geo"]/meta[@itemprop="latitude"]/@content').extract()
			item["longtitude"] = sel.xpath('div[@itemprop="contentLocation"]/div[@itemprop="geo"]/meta[@itemprop="longitude"]/@content').extract()
			data = sel.xpath('div[@class="resultData"]')
			item["property_type"] = data.xpath('div[@class="hideinSearchresults"]/h4/a/@title').extract()
			item["address"] = data.xpath('div[@class="hideinSearchresults"]/h5/strong/text()').extract()
			item["city"] = data.xpath('div[@class="hideinSearchresults"]/h5/span[@class = "city"]/text()').extract()
			#item["askprice"] = data.xpath('div[@class="hideinSearchresults"]/p/strong/text()').extract()
			next_url = data.xpath('div[@class="hideinBookmarks"]/h4/a/@href').extract()[0]
			next_url = "http://duproprio.com" + next_url
			request = Request(next_url, callback=self.parse_next)
			request.meta["item"] = item
			yield request

	def parse_next(self, response):
		item = response.meta['item']
		#print response
		#print response.xpath('//div[@id="details"]/div[@class="content"]/div[@class="dynamicList"]/ul[@class="left"]/@class').extract()
 		item["living_area"] = response.xpath('//div[@id="details"]/div[@class="content"]/div[@class="dynamicList"]/ul[@class="left"]/li/strong[contains(text(), "Aire habitable")]/../text()[last()]').extract()
 		item["year_built"] = response.xpath('//div[@id="details"]/div[@class="content"]/div[@class="dynamicList"]/ul[@class="right"]/li/strong[contains(text(), "de construction")]/../text()[last()]').extract()
		item["askprice"] = response.xpath('//div[@id="details"]/div[@class="content"]/div[@class="dynamicList"]/ul[@class="left"]/li/strong[contains(text(), "Prix demand")]/../text()[last()]').extract()
		item["num_parking"] = response.xpath('//div[@id="details"]/div[@class="content"]/div[@class="dynamicList"]/ul[@class="left"]/li/strong[contains(text(), "Nombre de stationnement int")]/../text()[last()]').extract()
		item["num_bath"] = response.xpath('//div[@id="details"]/div[@class="content"]/div[@class="dynamicList"]/ul[@class="right"]/li/strong[contains(text(), "Nombre de salles de bain")]/../text()[last()]').extract()
		item["num_room"] = response.xpath('//div[@id="details"]/div[@class="content"]/div[@class="dynamicList"]/ul[@class="right"]/li/strong[contains(text(), "Nombre total de pi")]/../text()[last()]').extract()
		item["num_bed"] =  response.xpath('//div[@id="details"]/div[@class="content"]/div[@class="dynamicList"]/ul[@class="right"]/li/strong[contains(text(), "Nombre de chambres")]/../text()[last()]').extract()
		return cleanDuPropData(item)

	def start_requests(self):
		for page in range(1,240):
			page_string = str(page)
			yield Request(self.start_url % page_string, dont_filter=True)

class DuPropSoldSpider(scrapy.Spider):
	name = "DuPropSold"
	allowed_domains = ["duproprio.com"]
	start_url = "http://duproprio.com/search/?hash=/g-re=6/s-pmin=0/s-pmax=99999999/s-build=1/s-filter=sold/s-hide-sold=/s-mode=list/p-con=main/p-ord=date/p-dir=DESC/pa-ge=%s/"
	def parse(self, response):
		for sel in response.xpath('//ol[@id="searchResults"]/*'):
			item = Property()		
			item["data_code"] = sel.xpath('@data-code').extract()
			if(len(item["data_code"]) == 0):
				continue
			item["latitude"] = sel.xpath('div[@itemprop="contentLocation"]/div[@itemprop="geo"]/meta[@itemprop="latitude"]/@content').extract()
			item["longtitude"] = sel.xpath('div[@itemprop="contentLocation"]/div[@itemprop="geo"]/meta[@itemprop="longitude"]/@content').extract()
			data = sel.xpath('div[@class="resultData"]')
			item["property_type"] = data.xpath('div[@class="hideinSearchresults"]/h4/a/@title').extract()
			item["address"] = data.xpath('div[@class="hideinSearchresults"]/h5/strong/text()').extract()
			item["city"] = data.xpath('div[@class="hideinSearchresults"]/h5/span[@class = "city"]/text()').extract()
			#item["askprice"] = data.xpath('div[@class="hideinSearchresults"]/p/strong/text()').extract()
			item["sold_date"] = data.xpath('div[@class="infoSold"]/p[contains(text(), "Vendu en")]/strong[contains(text(),"-")]/text()').extract()
			#print item["sold_date"]
			next_url = data.xpath('div[@class="hideinBookmarks"]/h4/a/@href').extract()[0]
			next_url = "http://duproprio.com" + next_url
			request = Request(next_url, callback=self.parse_next)
			request.meta["item"] = item
			yield request

	def parse_next(self, response):
		item = response.meta['item']
		#print response
		#print response.xpath('//div[@id="details"]/div[@class="content"]/div[@class="dynamicList"]/ul[@class="left"]/@class').extract()
 		item["living_area"] = response.xpath('//div[@id="details"]/div[@class="content"]/div[@class="dynamicList"]/ul[@class="left"]/li/strong[contains(text(), "Aire habitable")]/../text()[last()]').extract()
 		item["year_built"] = response.xpath('//div[@id="details"]/div[@class="content"]/div[@class="dynamicList"]/ul[@class="right"]/li/strong[contains(text(), "de construction")]/../text()[last()]').extract()
		item["askprice"] = response.xpath('//div[@id="details"]/div[@class="content"]/div[@class="dynamicList"]/ul[@class="left"]/li/strong[contains(text(), "Prix demand")]/../text()[last()]').extract()
		item["num_parking"] = response.xpath('//div[@id="details"]/div[@class="content"]/div[@class="dynamicList"]/ul[@class="left"]/li/strong[contains(text(), "Nombre de stationnement int")]/../text()[last()]').extract()
		item["num_bath"] = response.xpath('//div[@id="details"]/div[@class="content"]/div[@class="dynamicList"]/ul[@class="right"]/li/strong[contains(text(), "Nombre de salles de bain")]/../text()[last()]').extract()
		item["num_room"] = response.xpath('//div[@id="details"]/div[@class="content"]/div[@class="dynamicList"]/ul[@class="right"]/li/strong[contains(text(), "Nombre total de pi")]/../text()[last()]').extract()
		item["num_bed"] =  response.xpath('//div[@id="details"]/div[@class="content"]/div[@class="dynamicList"]/ul[@class="right"]/li/strong[contains(text(), "Nombre de chambres")]/../text()[last()]').extract()
		return cleanDuPropData(item)

	def start_requests(self):
		for page in range(1,885):
			page_string = str(page)
			yield Request(self.start_url % page_string, dont_filter=True)

def cleanDuPropData(item):
	if(len(item["living_area"]) > 0 and item["living_area"][0].find("x") != -1):
		num = item["living_area"][0].split("x")
		item["living_area"] = float(num[0])*float(num[1])
	if(len(item["num_bed"]) > 0):
		item["num_bed"] = item["num_bed"][0].replace(' ', '')
	if(len(item["num_bath"]) > 0):
		item["num_bath"] = item["num_bath"][0].replace(' ', '')
	if(len(item["num_room"]) > 0):
		item["num_room"] = item["num_room"][0].replace(' ', '')
	if(len(item["num_parking"]) > 0):
		item["num_parking"] = item["num_parking"][0].replace(' ', '')
	if(len(item["askprice"]) > 0):
		item["askprice"] = item["askprice"][0].replace(' ', "").replace("$","").replace(",","")
	if(len(item["living_area"]) != 0):
		item["living_area"] = item["living_area"][0].split(" m")[0]
		if(len(item["living_area"].split("(")) > 1):
			item["living_area"] = item["living_area"].split("(")[1]
	return item


class RoyalHouseSpider(scrapy.Spider):
	name="RoyalHouse"
	allowed_domains = ["royallepage.ca"]
	start_url = "http://www.royallepage.ca/search/homes/qc/montreal/%s/?csrfmiddlewaretoken=jm18zhjCssxjXR6Bg3aluTVFnt25rIs1&min_price=0&max_price=5000000&min_leaseprice=0&max_leaseprice=2000&property_type=7&house_type=&features=&listing_type=&lat=45.5086699&lng=-73.55399249999999&bypass=&display_type=gallery-view&tier2=False&tier2_proximity=0&search_str=Montreal+QC+Canada&beds=0&baths=0&sfproperty_type=7&sfproperty_type=8&transactionType=SALE&address=Montreal&method=homes&address_type=city&city_name=Montreal&prov_code=QC&sortby=#.VGwKtPnxqpd"

	def parse(self, response):
		for sel in response.xpath('//ul[@class="result-list"]/*'):
			item = Property()		
			item["data_code"] = sel.xpath('section/@data-id').extract()
			data = sel.xpath('section/div[@class="text-holder"]')
			item["property_type"] = data.xpath('ul[@class="list"]/li[1]/text()').extract()
			item["address"] = data.xpath('address/a/text()').extract()
			item["askprice"] = data.xpath('em[@class="price"]/text()').extract()
			next_url = data.xpath('address/a/@href').extract()[0]
			request = Request(next_url, callback=self.parse_next)
			request.meta["item"] = item
			yield request

	def parse_next(self, response):
		item = response.meta['item']
		#print response
		#print response.xpath('//div[@class="price-holder"]/h1/text()').extract()
 		item["living_area"] = response.xpath('//ul[@class="property-features"]/li[@class="label" and contains(text(),"Floor Space (approx):")]/following-sibling::li[1]/text()').extract()
 		item["year_built"] = response.xpath('//ul[@class="property-features"]/li[@class="label" and contains(text(),"Built in:")]/following-sibling::li[1]/text()').extract()
		item["city"] = response.xpath('//div[@class="price-holder"]/h1/text()').extract()
		item["num_parking"] = response.xpath('//ul[@class="property-features"]/li[@class="label" and contains(text(),"No. of Parking Spaces:")]/following-sibling::li[1]/text()').extract()
		item["num_bath"] = response.xpath('//ul[@class="property-features"]/li[@class="label" and contains(text(),"Bathrooms:")]/following-sibling::li[1]/text()').extract()
		item["num_bed"] = response.xpath('//ul[@class="property-features"]/li[@class="label" and contains(text(),"Bedrooms:")]/following-sibling::li[1]/text()').extract()
		return cleanRoyalData(item)
	

	def start_requests(self):
		for page in range(1,150):
			page_string = str(page)
			yield Request(self.start_url % page_string, dont_filter=True)

class RoyalCondoSpider(scrapy.Spider):
	name="RoyalCondo"
	allowed_domains = ["royallepage.ca"]
	start_url = "http://www.royallepage.ca/search/homes/qc/montreal/%s/?csrfmiddlewaretoken=jm18zhjCssxjXR6Bg3aluTVFnt25rIs1&min_price=0&max_price=5000000&min_leaseprice=0&max_leaseprice=2000&property_type=8&house_type=&features=&listing_type=&lat=45.5086699&lng=-73.55399249999999&bypass=&display_type=gallery-view&tier2=False&tier2_proximity=0&search_str=Montreal+QC+Canada&beds=0&baths=0&sfproperty_type=7&sfproperty_type=8&transactionType=SALE&address=Montreal&method=homes&address_type=city&city_name=Montreal&prov_code=QC&sortby=#.VGwKtPnxqpd"

	def parse(self, response):
		for sel in response.xpath('//ul[@class="result-list"]/*'):
			item = Property()		
			item["data_code"] = sel.xpath('section/@data-id').extract()
			data = sel.xpath('section/div[@class="text-holder"]')
			item["property_type"] = data.xpath('ul[@class="list"]/li[1]/text()').extract()
			item["address"] = data.xpath('address/a/text()').extract()
			item["askprice"] = data.xpath('em[@class="price"]/text()').extract()
			next_url = data.xpath('address/a/@href').extract()[0]
			request = Request(next_url, callback=self.parse_next)
			request.meta["item"] = item
			yield request

	def parse_next(self, response):
		item = response.meta['item']
		#print response
		#print response.xpath('//div[@class="price-holder"]/h1/text()').extract()
 		item["living_area"] = response.xpath('//ul[@class="property-features"]/li[@class="label" and contains(text(),"Floor Space (approx):")]/following-sibling::li[1]/text()').extract()
 		item["year_built"] = response.xpath('//ul[@class="property-features"]/li[@class="label" and contains(text(),"Built in:")]/following-sibling::li[1]/text()').extract()
		item["city"] = response.xpath('//div[@class="price-holder"]/h1/text()').extract()
		item["num_parking"] = response.xpath('//ul[@class="property-features"]/li[@class="label" and contains(text(),"No. of Parking Spaces:")]/following-sibling::li[1]/text()').extract()
		item["num_bath"] = response.xpath('//ul[@class="property-features"]/li[@class="label" and contains(text(),"Bathrooms:")]/following-sibling::li[1]/text()').extract()
		item["num_bed"] = response.xpath('//ul[@class="property-features"]/li[@class="label" and contains(text(),"Bedrooms:")]/following-sibling::li[1]/text()').extract()
		return cleanRoyalData(item)
	

	def start_requests(self):
		for page in range(1,150):
			page_string = str(page)
			yield Request(self.start_url % page_string, dont_filter=True)


def cleanRoyalData(item):
	if(len(item["living_area"]) > 0):
		item["living_area"] = item["living_area"][0].split(" Sq")[0]
	if(len(item["askprice"]) > 0):
		item["askprice"] = item["askprice"][0].split("\t")[3].split("\n")[0].split("$")[1].replace(",", "")
	if(len(item["num_bed"]) > 0 and item["num_bed"][0].find("+") != -1):
		num = item["num_bed"][0].split("+")
		item["num_bed"] = float(num[0])+float(num[1])
	return item


""
#Doesn't quite work at the moment. Redirected by site...
class RealtorSpider(scrapy.Spider):
	name="Realtor"
	allowed_domains = ["http://www.realtor.ca/"]
	start_url = "http://www.realtor.ca/Map.aspx#CultureId=2&ApplicationId=1&RecordsPerPage=9&MaximumResults=9&PropertyTypeId=300&TransactionTypeId=2&SortOrder=A&SortBy=1&LongitudeMin=-73.79614448547366&LongitudeMax=-73.47239112854007&LatitudeMin=45.41721735945016&LatitudeMax=45.6060789209926&PriceMin=0&PriceMax=0&BedRange=0-0&BathRange=0-0&ParkingSpaceRange=0-0&viewState=l&CurrentPage=%s"

	def parse(self, response):
		for sel in response.xpath('//div[@id="listViewContent"]/*'):
			print sel
			item = Property()
			addr = sel.xpath('//div[@class="m_property_lst_hdr_rgt"]/a/span/text()').extract()		
			addr = addr.split(",")
			#item["data_code"] = sel.xpath('//div[@class="m_property_lst_hdr_rgt"]/a/span/text()').extract()
			item["property_type"] = sel.xpath('//div[contains(@id,"list_lst_buildtype")]/text()').extract()
			item["address"] = addr[0]
			item["city"] = addr[-2]
			item["askprice"] = sel.xpath('//div[@class="m_property_lst_cnt_property_price"]/text()').extract()
			yield item
	

	def start_requests(self):
		for page in range(1,10):
			page_string = str(page)
			yield Request(self.start_url % page_string, dont_filter=True)

