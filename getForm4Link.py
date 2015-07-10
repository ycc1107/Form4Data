import urllib2
import urllib
import simplejson
from BeautifulSoup import BeautifulSoup

def googleAPICall(ticker):   
    res = []  
    quote = ticker + ' form4'   
    userInput = urllib.quote(quote)    
    #nyu
    KEY = "AIzaSyC5WA2gfeLrJrXRvhDkaAuKHLGiPGSpuqY"
    CX = "015476964111987883949:xuenin0mbdu"
    #ycc1107
    #CX ='015234309602230089587:00ju8drfads'
    #KEY ='AIzaSyBjal_PLwCWYu54d9RC_S5zQHsJYGlYJxM'
    url = ('https://www.googleapis.com/customsearch/v1?'    
               'key=%s'
               '&cx=%s'
               '&alt=json'
               '&q=%s'
               '&num=10'
               '&start=%d')%(KEY,CX,userInput,1) 
    print(url)       
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    results = simplejson.load(response)
    webs = results['items']
      
    
         
    with open('linkContain.txt','a') as f:
        for web in webs:
            res.append(web["link"])  
            print >> f,web['link']

    cleanLinks(res)

    
def cleanLinks(links):
    res = []
    pattern = r'^.*(www.secform4.com/insider-trading/).*$'
    matcher = re.compile(pattern)
    for link in links:
        if matcher.match(link):
            res += link,
    with open('form4Lines.txt','w') as f:
        for link in res:
            print >> f,link


def run():
    tickerLst,links = [],[]
    with open('tickerList.txt','r') as f:
        for i in f.read().split('\n')[:100]:
            print(i)
            tickerLst.append(i.strip('\n'))

    for ticker in tickerLst:
        googleAPICall(ticker)


if __name__=="__main__":
    run()