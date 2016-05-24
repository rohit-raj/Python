'''
	Web Crawler for Shopping.com
'''
import sys
import os
from lxml import html
import requests
import string
import unittest

class featureCollect:
	def __init__(self):
		self.productTree = dict()
		self.count = 0

	def collect (self, url):
		headers = {'user-agent': 'Mozilla/5.0 (compatible; CrawlBot/2.1; +http://www.google.com/bot.html)'}
		try:
			page = requests.get(url, headers=headers)
		except Exception, e:
			raise e
			return 0
		
		tree = html.fromstring(page.text)
		productList = tree.find_class ("productName")
		count = len(productList)
		if count > 0 :
			self.count = self.count + count
			return 1
		else :
			return 0
		
def crawl(page, product):
	url = "http://www.shopping.com/products"

	collector = featureCollect()
	if page == 0:
		args = 1
	else:
		args = 2

	#args = len(sys.argv) - 1

	if args == 1 :
		url1 = url + '?KW=' + product
		collector.collect(url1)
		next = 1
		x = 2
		while (next == 1):
			#print 'page ::: ', x - 1
			url1 = url + '~PG-' + str(x) + '?KW=' + product
			next = collector.collect (url1)
			x = x + 1

	elif args == 2 :
		url1 = url + '~PG-' + str(page) + '?KW=' + product
		collector.collect(url1)
	else :
		print 'provide one article name as argument or provide page number with article name::eg: 2 deo'

	print ':::::: Total product count ::::::'
	print collector.count


class parseTests(unittest.TestCase):
	def testOne(self):
		self.failUnless(crawl(2, "deo"))
	# def testTwo(self):
	# 	self.failIf(crawl("deo"))
	# def testThree(self):
	# 	self.failIf(parse("ldap://[2001:db8::7]/c=GB?objectClass?one"))
	# def testFour(self):
	# 	self.failIf(parse("https://www.ietf.org/rfc/index.html?user=1#page"))
	# def testFive(self):
	# 	self.failIf(parse("http://www.ietf.org/rfc/rfc2396.txt"))

def main():
	unittest.main()


if __name__ == "__main__":
	main()