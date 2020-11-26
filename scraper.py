import requests
from bs4 import BeautifulSoup
import random
import wikipedia
import html5lib
import warnings
import time

warnings.filterwarnings('ignore')

def endlessScrapeFromSearch(searchQuery):
	scrapeSite(getUrlFromSearch(searchQuery))

def scrapeSite(url):
	try:
		response = requests.get(url = url)
	except:
		return
	soup = BeautifulSoup(response.content,
		'html.parser')
	
	title = soup.find(id="firstHeading")
	print(title.text)

	allLinks = soup.find(id="bodyContent").find_all("a")
	random.shuffle(allLinks)
	linkToScrape = 0
	for link in allLinks:
		# We are only interested in other wiki articles
		try:
			if link['href'].find("/wiki/") == -1: 
				continue
		except KeyError:
			return
		# Use this link to scrape
		linkToScrape = link
		break
	
	time.sleep(1)
	try:
		scrapeSite("https://en.wikipedia.org" + linkToScrape['href'])
	except TypeError: 
		return
		
def search(search):
	return wikipedia.search(search)

def getUrl(page):
	soup = BeautifulSoup(wikipedia.page(page).url, features="html.parser")
	return soup

def getUrlFromSearch(searchQuery):
	searchResults = search(searchQuery)
	for result in searchResults:
		try:
			return getUrl(result)
		except:
			pass