import requests
from bs4 import BeautifulSoup


# Collect and parse first page
page = requests.get('https://www.bet365.com/#/IP/')
soup = BeautifulSoup(page.text, 'html.parser')

# Pull all text from the BodyText div
artist_name_list = soup.findAll('div',{'class':'ipn-Classification ipn-Classification-open'})
print(len(artist_name_list))

# Pull text from all instances of <a> tag within BodyText div
for artist_name in artist_name_list:
    print(artist_name.get_text())
