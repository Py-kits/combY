from bs4 import BeautifulSoup
import urllib.request
import lxml.html
import lxml.html.soupparser


CombYFile = urllib.request.urlopen("https://news.ycombinator.com/newest")
CombYHtml = CombYFile.read()
CombYFile.close()

search = BeautifulSoup(CombYHtml, "lxml")
#CombYAll = search.find_all("a", {"class": "storylink"})
#for hyperlinks in search.find_all('a'):
#    print (hyperlinks.get('href'))
# Missing text file output