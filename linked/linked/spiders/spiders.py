from scrapy.http import Request
from scrapy.spiders import BaseSpider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor 
import pandas as pd 
import re
from linked.items import LinkedItem

email = re.compile('([\w\-\.]+@(\w[\w\-]+\.)+[\w\-]+)')

class linkSpider(CrawlSpider):
	name = 'linkedin'
	allowed_urls = ["www.reddit.com"]
	start_urls = ["https://www.reddit.com/"]

	rules = (
		Rule(LinkExtractor(), callback = 'printResponse', follow = True),)


	def printResponse(self, response):
		emails = email.findall(response.body)
		if len(emails) > 0:
			item = LinkedItem()
			for x in emails:
				item['email'] = emails
				return item