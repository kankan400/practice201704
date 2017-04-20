#unicode error!!
# see you

from HTMLParser import HTMLParser
import urllib2
import sys

class GetLink(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.link_flag = False
		self.link_path = ''

	def handle_starttag(self, tag, attrs):
		if tag == 'a':
			for name, value in attrs:
				if name == 'href':
					self.link_path = value.encode()
					self.link_flag = True

	def handle_data(self, data):
		if self.link_flag:
			print "%s   %s" %(self.link_path, data)
			self.link_flag = False

	def handle_endtag(self, tag):
		pass

def main(argv):
	if not argv[1]:
		print "Please input target URL in arg1"
		sys.exit()

	response = urllib2.urlopen(argv[1])
	link_parser = GetLink()
	link_parser.feed(response.read())
	link_parser.close()
	

if __name__ == '__main__':
	main(sys.argv)	
