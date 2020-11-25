import scraper
import warnings
import wikipedia

warnings.filterwarnings('ignore')
try:
	scraper.getUrl((scraper.search("Center High School"))[0])
except wikipedia.exceptions.DisambiguationError:
	print(scraper.getUrl((scraper.search("Center High School"))[1]))
