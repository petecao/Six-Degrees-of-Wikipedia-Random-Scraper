import scraper
import warnings

warnings.filterwarnings('ignore')
i = 0
try:
	scraper.getUrl((scraper.search("Center High School"))[i])
except Exception:
	print(scraper.getUrl((scraper.search("Center High School"))[i+1]))
with warnings.catch_warnings():
	warnings.simplefilter("ignore")