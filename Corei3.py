from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://fortebet.ug/?#/app/offer/top")
elem = driver.find_element_by_id("login")
elem.send_keys("")

elem2 = driver.find_element_by_id("password")
elem2.send_keys("")



login_attempt=driver.find_element_by_class_name("btn btn-highlight ng-binding").click()

