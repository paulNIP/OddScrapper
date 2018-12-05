from urllib.request import urlopen
import random
from bs4 import BeautifulSoup
html = urlopen("http://soccervista.com")

bsObj = BeautifulSoup(html,'html.parser')

# array to store links
vistalinks=[]
#storing soccervista links in an array
for link in bsObj.findAll('a'):
	if 'href' in link.attrs:
		vistalinks.append(link.attrs['href'])
		#print(link.attrs['href'])
		
#print vista links
#print(vistalinks)


# select Random leagues to bet on
option1 = random.choice(vistalinks)
print(option1)

option1='/England-Championship-2018_2019-856081.html'

#check if string contains soccervista
if option1=="https://www.soccervista.com"+option1:
	#proceed to page	
	print(option1)
	#check tips on the given page
	html0=urlopen(option1)
	bsObj0=BeautifulSoup(html0,'html.parser')
	tips=bsObj0.findAll("table",{'class':'upcoming'})
	print(len(tips))
	for tip in tips:
		print(tip.find('tr',{'class':'predict'}).text)

		

elif option1!="https://www.soccervista.com"+option1:
	option2="https://www.soccervista.com"+option1
	print(option2)
	#check tips on the given page
	html0=urlopen(option2)
	bsObj0=BeautifulSoup(html0,'html.parser')
	tips=bsObj0.findAll("table",{'class':'upcoming'})
	print(len(tips))
	for tip in tips:
		print(tip.find('tr',{'class':'predict'}).text)

		

	
else:
	print("Booyaka")



    
#check tips on the given page
# html0 = urlopen(option1)
# bsObj0 = BeautifulSoup(html0,'html.parser')
# tips = bsObj.findAll("tr")
# for tip in tips:
# 	print(tip.get_text())









