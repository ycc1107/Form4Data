import re
import urllib2
from BeautifulSoup import BeautifulSoup as bs

def getForm4Link():
	res = []
	with open('linkContain.txt','r') as f:
		pattern = r'^.*(www.secform4.com/insider-trading/).*$'
		matcher = re.compile(pattern)
		for link in f:
			if matcher.match(link):
				res += link,
	return res
def getContainOfLink(links):
	for link in links:
		respone = urllib2.urlopen(link)
		html = respone.read()
		soup = bs(html)
		name = soup.findAll('div',attrs = {'class':'tag'})[0].findAll('b')[0].text
		name = ''.join(name.split(' ')) + '.txt'
		with open(name,'w') as f:
			print >> f,html




def main():
	links = getForm4Link()
	print(links[0])
	getContainOfLink(links)
	

if __name__ == "__main__":main()
				