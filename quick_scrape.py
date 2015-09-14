import re
import urllib
from bs4 import BeautifulSoup

config      = open("scrape.config","r")
file_string = config.read()
config_patt = re.compile("Search\s(.*)\sfor|of\s(.*)")
config_splt = re.findall(config_patt,file_string)

searches = []
for i in range(0,len(config_splt),2):
	if config_splt[i][1] == "":
		searches = searches + [(config_splt[i][0],config_splt[i+1][1])]

for search in searches:
	search_patt   = re.compile(search[1])
	site_string   = urllib.urlopen(search[0]).read()
	site_soup     = BeautifulSoup(site_string)
	site_text     = `site_soup.get_text()`
	search_string = re.findall(search_patt,site_text)
	print search_string