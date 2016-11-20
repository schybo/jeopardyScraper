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

url = showUrls[1];
newPage = urllib2.urlopen(url);
newSoup = BeautifulSoup(newPage);

thirdUrls = newSoup.find_all('a')
newUrls = [url for url in thirdUrls if 'buttonlink' in url]

print newUrls