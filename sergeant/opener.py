from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

chromedriver = "./chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

def _cp_open(url="localhost:4545/paper/new"):
	driver.get(url)

def _cp_close():
	driver.close()

def _credentials(uname="fizz", email_id="buzz@beer.com"):
	c_name = driver.find_element_by_id('candidateName')
	c_name.send_keys(uname)
	email = driver.find_element_by_id('candidateEmail')
	email.send_keys(email_id)
	button = driver.find_element_by_xpath("//*[contains(text(), 'Join as candidate')]")
	button.send_keys(Keys.RETURN)

_cp_open()
_credentials()
# _cp_close()

'''
candidateName
candidateEmail
interviewerName
accessCode
'''
