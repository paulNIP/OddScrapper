from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get("https://fortebet.ug/#/app/offer/top") 
time.sleep(10)
username = browser.find_element_by_id("login")
password = browser.find_element_by_id("password")
username.send_keys("Paul85alex")
password.send_keys("polo1990")
login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
login_attempt = driver.find_element_by_class_name('btn btn-highlight ng-binding').click()
login_attempt.submit()