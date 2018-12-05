#scrap Live odds from Bet 365

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://www.bet365.com/#/IP/")

bsObj = BeautifulSoup(html)

# array to store links
vistalinks=[]
#storing soccervista links in an array
for link in bsObj.findAll('a'):
	if 'href' in link.attrs:
		vistalinks.append(link.attrs['href'])
		#print(link.attrs['href'])
		
#print vista links
print(vistalinks)



