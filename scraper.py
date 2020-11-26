import requests
from bs4 import BeautifulSoup
import random
import wikipedia
import html5lib
import warnings

warnings.filterwarnings('ignore')



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