from requests import get

url = 'https://www.bet365.com/#/IP/'

response = get(url)
print(response.text[:500])

from bs4 import BeautifulSoup

html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)

movie_containers = html_soup.find_all("div",{"class":"ipn-Classification ipn-Classification-open"})
print(type(movie_containers))
print(len(movie_containers))

