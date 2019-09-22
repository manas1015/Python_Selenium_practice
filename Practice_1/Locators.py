from selenium import webdriver
import time



chrome = webdriver.Chrome(r'F:\Py browser engine\chromedriver_win32\chromedriver.exe')
chrome.maximize_window()
chrome.get("https:facebook.com")

# automation.set_window_size(1000,600)
title = chrome.title
print(title)

#send keys to the email field
chrome.find_element_by_id('email').send_keys('balaji.3257@gmail.com')

#send keys using xpath techniques
# chrome.find_element_by_xpath('//input[@class="inputtext" or @id="email"]').send_keys('balaji.3257@gmail.com')
#//input[@class="inputtext"]
# send keys to the password fiels

# //*[@id="email"]
chrome.find_element_by_id('pass').send_keys('12345')


# click the login button
chrome.find_element_by_id('loginbutton').click()

time.sleep(2)


# chrome.find_element_by_link_text('Recover Your Account').click()

chrome.find_element_by_partial_link_text('Recover Your').click()


time.sleep(4)
chrome.quit()