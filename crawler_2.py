'''
	Web Crawler for Shopping.com
'''
import sys
import os
from lxml import html
import requests
import string

class featureCollect:
	def __init__(self):
		self.productTree = dict()
		self.count = 0

	def collect (self, url):
		headers = {'user-agent': 'Mozilla/5.0 (compatible; CrawlBot/2.1; +http://www.google.com/bot.html)'}
		page = requests.get(url, headers=headers)
		tree = html.fromstring(page.text)
		productList = tree.find_class ("productName")
		count = len(productList)
		if count > 0 :
			self.count = self.count + count
			return 1
		else :
			return 0

	def directCollect(self, url):
		page = requests.get(url)
		tree = html.fromstring(page.text)
		productCount = tree.find_class ("numTotalResults")
		for product in productCount:
			cnt = product.xpath('text()')
			self.count = cnt[0].split()[len(cnt[0].split()) -1]

def main():
	url = "http://www.shopping.com/products"

	args = len(sys.argv) -1
	collector = featureCollect()
	if args == 1 :
		url1 = url + '?KW=' + sys.argv[1]
		collector.directCollect(url1)
	elif args == 2 :
		url1 = url + '~PG-' + sys.argv[1] + '?KW=' + sys.argv[2]
		collector.collect(url1)
	else :
		print 'Provide one article name as argument or provide page number with article name::'
		print 'eg: 2 deo'

 	print ':::::: Total product count ::::::'
 	print collector.count

if __name__ == "__main__":
	main()