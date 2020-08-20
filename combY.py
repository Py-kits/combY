from bs4 import BeautifulSoup
import urllib.request
import lxml.html
import lxml.html.soupparser


CombYFile = urllib.request.urlopen("https://news.ycombinator.com/newest")
CombYHtml = CombYFile.read()
CombYFile.close()

search = BeautifulSoup(CombYHtml, "lxml")
CombYAll = search.find_all("a", {"class": "storylink"})
for hyperlinks in search.find_all('a'):
    print (hyperlinks.get('href'))
# Currently missing text file output.  (listings.txt)
# Current code lists all text lines with the a href property 
# Code should output 
# 1) Listing name for articles
# 2) Url for listed articles