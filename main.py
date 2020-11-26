import scraper
import gui

if __name__ == "__main__":
	while False:
		query = input("What do you want to search for? ")
		if query.lower() == "quit":
			break
		print()
		scraper.endlessScrapeFromSearch(query)
		print()

