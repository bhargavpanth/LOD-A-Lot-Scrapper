from bs4 import BeautifulSoup
import urllib
from time import sleep
from fake_useragent import UserAgent

# https://hdt.lod.labs.vu.nl/triple?page=1&page_size=100&g=%3Chttps%3A//hdt.lod.labs.vu.nl/graph/BAG%3E

class ScrapeLODAaLot():
	
	"""
	docstring for ScrapeLODAaLot

	# start index = 1
	# end index = 9228776
	"""

	"""
	9228776 request over the span of 9 days
	"""

	def __init__(self, start, end):
		self.start = start
		self.end = end

	# re-write in observable
	# currently not following good design pattern


	def scrape(self):
		head = 'https://hdt.lod.labs.vu.nl/triple?page='
		tail = '&page_size=100&g=%3Chttps%3A//hdt.lod.labs.vu.nl/graph/BAG%3E'
		for x in xrange(int(self.start), int(self.end)):
			_url = head + str(x) + tail
			html_content = self.request_for_page(_url)
			print html_content
			self.get_tuples(html_content)
		# print 'URL lsit exhausted - index crossed'


	def request_for_page(self, url):
		return urllib.urlopen(url).read()
		# user_agent = UserAgent()
		# print user_agent.random
		# print url
		# try:
		# 	# req = urllib2.Request(url)
		# 	# req.add_header(user_agent.random)
		# 	response = urllib.urlopen(url)
		# except Exception as e:
		# 	pass
		# else:
		# 	return response.read()
		# finally:
		# 	pass


	def get_tuples(self, content):
		try:
			soup = BeautifulSoup(content, 'html.parser')
		except Exception as e:
			raise
			print 'unable to fetch'
		else:
			for tr in soup.find_all('tr')[2:]:
				tds = tr.find_all('td')
				print (tds[0].text, tds[1].text, tds[2].text)
		
		# for tr in soup.find_all('tr')[2:]:
		




def main():
	test = ScrapeLODAaLot(1,2).scrape()


if __name__ == '__main__':
	main()
		