import requests
from bs4 import BeautifulSoup
import random
import wikipedia
import html5lib




def search(search):
	print(wikipedia.search(search))
	return wikipedia.search(search)

def getUrl(page):
	soup = BeautifulSoup(wikipedia.page(page).url, features="html.parser")
	return soup
