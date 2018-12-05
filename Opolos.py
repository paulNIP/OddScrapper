from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://soccervista.com")

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



