# -*- coding: utf-8 -*-
import scrapy
import string


class YlpSpider(scrapy.Spider):
    name = "ylp"
    allowed_domains = ["gelbeseiten.de"]
    alphabets = string.ascii_lowercase
    start_urls = ['https://www.gelbeseiten.de/Suche/'+ str(i)+'/Bundesweit/Seite-'+ str(x)
    for i in alphabets
        for x in range (1,3000)]
    
    def parse(self, response):
		#companies = response.xpath('//*[@class="name m08_name"]')
		
		for company in response.css('article'):
			name = company.xpath('.//span[@itemprop="name"]//text()').extract_first()
			address = company.xpath('.//span[@itemprop="streetAddress"]//text()').extract_first()
			postalcode = company.xpath('.//span[@itemprop="postalCode"]//text()').extract_first()
			addressLocality = company.xpath('.//span[@itemprop="addressLocality"]//text()').extract_first()
			phone = company.xpath('.//span[@class="nummer"]//text()').extract_first()
			mail = company.xpath('.//a[@class="link email_native_app"]/@href').extract()
			branchen = company.xpath('.//div[@data-role="branchen"]/div/span/text()').extract_first()


			yield{'Name':name,'Address':address,'PLZ':postalcode,'Ort':addressLocality,'Tel':phone, 'Mail':mail, 'Branche': branchen }