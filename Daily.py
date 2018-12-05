from selenium import webdriver
from bs4 import BeautifulSoup
import time, re, string
from urllib.request import urlopen
import random
from bs4 import BeautifulSoup

# change path as needed; can use other browsers
browser = webdriver.Firefox()

url = 'http://flashscore.com'
browser.get(url)

time.sleep(10) #extra time to let all JS on site load

#returns site HTML and encodes to ascii for BeautifulSoup


link = browser.find_element_by_xpath('//*[@id="fscon"]/ul/li[5]/span/a').click()

#html_of_interest=browser.execute_script('return arguments[0].innerHTML',link)
time.sleep(5)


html_of_interest=browser.page_source
sel_soup=BeautifulSoup(html_of_interest, 'html.parser')

#print list of teams playing
#rowcount=len(browser.find_element_by_xpath('//*[@id="g_1_rgXBwzaS"]'))
time.sleep(5)
# //*[@id="g_1_rgXBwzaS"]
# //*[@id="g_1_MgXQfyU2"]
todays_tables=browser.find_elements_by_xpath('//*[@id="fs"]/div[2]/table[1]/tbody')


for today in todays_tables:
	cells = today.find_elements_by_tag_name('tr')

	for cell in cells:

		data=cell.find_elements_by_tag_name('td')
		check=data[0].text
		start=data[1].text
		home=data[2].text
		away=data[3].text
		statsodd=data[4].text
		homeodd=data[5].text
		drawodd=data[6].text
		awayodd=data[7].text
		live=data[8].text

		#grab row indformation
		print(start)
		print(home)
		print(away)
		print(homeodd)
		print(drawodd)
		print(awayodd)

	#browser.find_element_by_xpath('//*[@id="g_1_rgXBwzaS"]/td[2]').text
	# home=browser.find_element_by_xpath('//*[@id="g_1_rgXBwzaS"]/td[3]').text
	# away=browser.find_element_by_xpath('//*[@id="g_1_rgXBwzaS"]/td[4]').text
	# homeodd=browser.find_element_by_xpath('//*[@id="g_1_rgXBwzaS"]/td[6]').text
	# drawodd=browser.find_element_by_xpath('//*[@id="g_1_rgXBwzaS"]/td[7]').text
	# awayodd=browser.find_element_by_xpath('//*[@id="g_1_rgXBwzaS"]/td[8]').text
	
#html = browser.execute_script(,url)
