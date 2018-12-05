#use selenium to scrape data with javascript content
from bs4 import BeautifulSoup
import requests
website_url=requests.get("http://flashscore.com").text
soup= BeautifulSoup(website_url,'html.parser')
print(soup)
My_tables=soup.find('tr',{'class':'tr-first stage-scheduled'})
print(My_tables)


	

		















