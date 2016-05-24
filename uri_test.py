import sys
import os
import string
import re
import unittest

'''
Parse URI
'''
class parseUri:
	def __init__(self):
		self.queryString = ''
		self.uri = ''
		self.url = ''
		self.urn = ''
		self.scheme = ''
		self.domain = ''
		self.path = ''
		self.fragment = ''
		self.resource = ''

	def findQueryString(self, uri):
		query = re.match('.*/\?', uri)
		print uri,' ::: after query ::: ', query
		if query:
			self.queryString = query
			print 'Matched'

	def findScheme(self, uri):
		self.uri = uri
		scheme = uri.split("://")
		if len(scheme) > 1:
			self.scheme = scheme[0]
			self.urn = scheme[1]
			self.findUrl(self.urn)			
		else:
			print 'No scheme in the URI'
			self.urn = uri
			self.findUrl(uri)

	
	def findUrl	(self, urn):
		url = urn.split("/")
		if len(url) > 1:
			self.url = self.scheme + '://' + url[0]
			self.domain = url[0]
			resources = urn.split(url[0])
			self.findResource(resources[1])
		else:
			print 'url not present'

	def findResource(self, resources):
		if "/" in resources:
			resource = resources.split("/")
			if resource > 1:
				path = ''
				for ress in resource:
					if "?" in ress or "#" in ress:
						if "?" in ress:
							ress = ress.split("?")[0]
						if "#" in ress:
							ress = ress.split("#")[0]
						if ress.find(".") > 0:
							self.resource = ress
							continue
						
					else:
						y = ress.find(".")
						if y > 0:
							self.resource = ress
							continue
						else:
							path = path + ress + '/'
				self.path = path
				reso = resource[len(resource) - 1]
				if "?" in reso:
					res = reso.split("?")
					self.queryString = res[1]
					if "#" in res[1]:
						self.queryString = res[1].split("#")[0]
				if "#" in reso:
					res = reso.split("#")
					self.fragment = res[1]

def parse(ur):
	uri = ur
	finder = parseUri()
	finder.findScheme(uri)
	print "uri::: ", finder.uri
	print "scheme::: ", finder.scheme
	print "url::: ", finder.url
	print "urn::: ", finder.urn
	print "domain::: ", finder.domain
	print "path::: ", finder.path
	print "resource::: ", finder.resource
	print "queryString::: ",finder.queryString
	print "fragment::: ",finder.fragment

class parseTests(unittest.TestCase):
	def testOne(self):
		self.failUnless(parse("ftp://ftp.is.co.za/rfc/rfc1808.txt"))
	def testTwo(self):
		self.failIf(parse("http://www.ietf.org/rfc/rfc2396.txt"))
	def testThree(self):
		self.failIf(parse("ldap://[2001:db8::7]/c=GB?objectClass?one"))
	def testFour(self):
		self.failIf(parse("https://www.ietf.org/rfc/index.html?user=1#page"))
	def testFive(self):
		self.failIf(parse("http://www.ietf.org/rfc/rfc2396.txt"))

def main():
	unittest.main()

if __name__ == '__main__':
	main()