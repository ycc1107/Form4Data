import urllib2,re
from BeautifulSoup import BeautifulSoup as bs

link ='http://www.investorguide.com/stock-list.php'
resp = urllib2.urlopen(link)
html = resp.read()

soup = bs(html)

items = soup.findAll('a',href = re.compile('/stock'))

res = []
for item in items:
	if len(item.text) < 5:
		res.append(item.text)
print(res[1:])

with open('to50ticker.txt','wb') as f:
	for i in res[1:]:
		print >> f,i