
from selenium import webdriver
import time
import openpyxl
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from random import randint


workbook = openpyxl.load_workbook('instagram.xlsx')
sheet = workbook["Sheet1"]

lcell = str(sheet['A1'].value)
pcell = str(sheet['B1'].value)
scell = str(sheet['C1'].value)


browser = webdriver.Chrome()
browser.get('https://www.instagram.com/')   
browser.maximize_window()

time.sleep(5)

email = browser.find_element_by_name('username')
email.send_keys(lcell)

password = browser.find_element_by_name('password')
password.send_keys(pcell)

password.submit()

time.sleep(5)

browser.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm').click()

searchelem = browser.find_element_by_css_selector('#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > input')
username = "friends"
searchelem.send_keys(username)

time.sleep(4)
browser.get('https://www.instagram.com/' + username + '/')

time.sleep(8)

followbutton = browser.find_element_by_css_selector('button')


if(followbutton.text == 'Follow'):
	followbutton.click()

time.sleep(3)
#clicking on followers button
browser.find_element_by_css_selector('#react-root > section > main > div > header > section > ul > li:nth-child(2) > a').click()


time.sleep(5)

#following all the followers in follower list
followerlist = browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
number_followers = len(followerlist.find_elements_by_css_selector('li'))
time.sleep(4)

followerlist.click()

actionchain = webdriver.ActionChains(browser)
c = 0
while(c < 50):
	time.sleep(2)
	total = followerlist.find_elements_by_css_selector('button')
	for t in total:
		if t.text == 'Follow':
			time.sleep(randint(1, 6))
			t.click()
			c = c + 1
			

	actionchain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
	number_followers = len(followerlist.find_elements_by_css_selector('li'))
	print(number_followers)
