import tkinter as tk
import pygubu
import scraper
import requests
from bs4 import BeautifulSoup
import random
import time


class MyApplication(pygubu.TkApplication):
	def _create_ui(self):
		self.builder = builder = pygubu.Builder()
		builder.add_from_file('Infinite Scraper GUI.ui')
		self.mainwindow = builder.get_object('frame_1', self.master)
		builder.connect_callbacks(self)

		

	def on_click(self):
		queryData = self.builder.get_object('search_bar')
		query = queryData.get()
		url = scraper.getUrlFromSearch(query)
		self.populateTree(url, 0)

	def populateTree(self, url, i):
		tree = self.builder.get_object('Results')
		try:
			response = requests.get(url = url)
		except:
			return
		soup = BeautifulSoup(response.content,
			'html.parser')
		title = soup.find(id="firstHeading")
		label = 'Link {0}'.format(i)
		columnData = (title, url)
		try:
			tree.insert('', tk.END, text = label,
				values = columnData)
		except UnicodeEncodeError:
			return
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
			self.populateTree("https://en.wikipedia.org" + linkToScrape['href'], i+1)
		except TypeError: 
			return

root = tk.Tk()
app = MyApplication(root)
app.run()