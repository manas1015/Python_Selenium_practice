from selenium import webdriver
import time
import config
import locator
varAutomation = webdriver.Chrome(config.driverpath)
varAutomation.maximize_window()
varAutomation.get(config.app_url)

# automation.set_window_size(1000,600)
# title = varAutomation.title
# print(title)
#
# varAutomation.find_element_by_xpath(locator.xpath_python).click()
# time.sleep(2)
# varAutomation.find_element_by_xpath(locator.xpath_java).click()
# time.sleep(1)
# varAutomation.find_element_by_xpath(locator.xpath_dbms).click()
# list1=[]
# sublist = [[]]
# list_of_elements=varAutomation.find_elements_by_xpath(locator.xpath_latest_updates)
# for single in list_of_elements:
#     list1.append(single.get_attribute('href')+" "+single.text)
# print(len(list1))
# for i in range(len(list1) + 1):
#
#
#     for j in range(i + 1, len(list1) + 1):
#
#         sub = list1[i:j]
#         sublist.append(sub)
#     print(sublist)
# ds=varAutomation.find_element_by_xpath('//a[@href="java-tutorial"]').text
# print(ds)
# popular_tutorial=varAutomation.find_elements_by_xpath(locator.xpath_popular_tutorial)
# list_of_elements=[]
# for single_item in popular_tutorial:
#     list_of_elements.append(single_item.text)
# print(list_of_elements)

learn_java=varAutomation.find_element_by_xpath(locator.xpath_learn_java).click()