#import the library used to query a website
import urllib2
#specify the url
wiki = "http://the-watch-series.to/serie/Jeopardy_%281984%29"
#Query the website and return the html to the variable 'page'
page = urllib2.urlopen(wiki)
#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup
#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page)

# print soup.prettify();

shows = soup.find_all('meta', attrs={"itemprop" : "url"})
showUrls = [show["content"] for show in shows]

# for showUrl in showUrls:
# 	print showUrl;

secondUrl = showUrls[2];
secondPage = urllib2.urlopen(secondUrl);
secondSoup = BeautifulSoup(secondPage);

secondPageUrls = secondSoup.find_all(lambda tag: tag.name == 'a' and 
                                   tag.get('class') == ['buttonlink'])

thirdUrl = secondPageUrls[1]['href'];

print thirdUrl

thirdPage = urllib2.urlopen(thirdUrl);
thirdSoup = BeautifulSoup(thirdPage);

thirdPageUrls = thirdSoup.find_all(href=True)

for thirdPageUrl in thirdPageUrls:
	print thirdPageUrl['href'];

# http://onwatchseries.to/cale.html?r=aHR0cDovL2dvcmlsbGF2aWQuaW4vNzVucncxamdhaWp5
# http://onwatchseries.to/cale.html?r=aHR0cDovL2dvcmlsbGF2aWQuaW4vNzVucncxamdhaWp5