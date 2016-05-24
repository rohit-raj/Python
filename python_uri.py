import sys
import os
import string
import re

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

def main():
	uri = sys.argv[1]
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
if __name__ == '__main__':
	main()