from selenium import webdriver
import time
import javatpointxpath
varAutomation = webdriver.Chrome(r'F:\Py browser engine\chromedriver_win32\chromedriver.exe')
varAutomation.maximize_window()
varAutomation.get("https://www.javatpoint.com")

# automation.set_window_size(1000,600)
title = varAutomation.title
print(title)