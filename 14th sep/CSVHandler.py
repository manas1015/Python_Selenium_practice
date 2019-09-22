
# from selenium import webdriver
# import time
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver import ActionChains
#
import logging
#
logging.basicConfig(level = logging.DEBUG , filename="")
#
# driver = webdriver.Chrome(r"F:\Py browser engine\chromedriver_win32\chromedriver.exe")
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("http://javatpoint.com")
#
#
#
# ListOfQuestion = driver.find_elements_by_xpath("//ol[@class='points']/li/a")
# xpath_listOfTut = "//h2[text()='Popular Tutorials']/parent::fieldset/descendant::div[@class='firsthomecontent']/a/div/img"
# ListOfHref = driver.find_elements_by_xpath(xpath_listOfTut)
# rows = []
# print(ListOfHref[0].get_attribute("src"))
# for i in ListOfHref:
#     newlist = []
#     newlist.append(i.get_attribute("src"))
#     rows.append(newlist)
#
# print(rows)

# //ol[@class='points']/li/a --> 269
# print(ListOfQuestion[0].text)
# for singleQues in ListOfQuestion:
#     print(singleQues.text)

import csv
filepath = r"C:\Users\admin\PycharmProjects\14th sep\CSV_Data\hi.csv"

header = ["Name", "Age", "Class"]
data_row1 = ["Balaji", "12", 5]
data_row2 = ["Faizal", "12", 5]
data_row3 = ["Manas", "12", 5]
data = [data_row1, data_row2, data_row3]

try:
    with open(filepath, 'w') as csvFile:
        writer = csv.writer(csvFile)
        # writer.write(["Source Images"])
        writer.writerows(data)
        csvFile.close()

except FileNotFoundError as error:
    print("Check the existence of the error "+ error)
# finally:
#     csvFile.close()

try:
    with open(filepath, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # if "balaji".title() in row:
            if len(row)>0:
                print(row)


        csvfile.close()


except Exception  as error:
   logging.error("Check the existence of the error " + str(error))
# finally:
#     csvfile.close()
#
# logging.info("Closing the driver")
# driver.quit()



