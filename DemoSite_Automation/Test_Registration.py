from selenium import webdriver
import time
from Data import TestData1 as td
import EnvConfig as env
from ObjectRepo1 import Locators1 as loc
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(env.DriverPATH)

driver.get(env.AppURL)

driver.maximize_window()

driver.implicitly_wait(10) # selenium inbuilt

#  Explicit wait mechanism - Advanced wait mechanism

initialEmailField = driver.find_element_by_id('email')
initialEmailField.send_keys(td.InitialEmailID)

goButton = driver.find_element_by_id('enterimg')
goButton.click()
driver.find_element_by_xpath(env.First_Name).send_keys(td.First_Name)
driver.find_element_by_xpath(env.Last_Name).send_keys(td.Last_Name)

Email=driver.find_element_by_xpath(loc.Email_Address)
Email.send_keys(td.Email)
phone=driver.find_element_by_xpath(loc.Phone).send_keys(td.phone)
Address=driver.find_element_by_xpath(loc.address)
Address.send_keys(td.address)

male=driver.find_element_by_xpath(loc.Male_Radio_Button)
female=driver.find_element_by_xpath(loc.Female_Radio_Button)
male.click()
time.sleep(2)
if male.is_selected():
    female.click()


cricket_CB = driver.find_element_by_id(loc.Cricket_Check_Box)
movies_CB = driver.find_element_by_id(loc.Movies_CB)
hockey_cb = driver.find_element_by_id(loc.Hockey_CB)

cricket_CB.click()
hockey_cb.click()

time.sleep(4)


if cricket_CB.is_selected():
    # Unselection Operation upon checkbox
    cricket_CB.click()

# if not movies_CB.is_selected() or not hockey_cb.is_selected():
#    #Selection process
#     movies_CB.click()

if not movies_CB.is_selected() and not hockey_cb.is_selected():
   #Selection process
    movies_CB.click()

# if not hockey_cb.is_selected():
#    #Selection process
#     hockey_cb.click()




driver.find_element_by_id(loc.Lang_DropDown).click()

driver.find_element_by_xpath(loc.Thai_DropDownSelection).click()
driver.find_element_by_xpath(loc.Swedish_DD_Selection).click()

time.sleep(1)

driver.find_element_by_xpath(loc.Thai_CloseButton).click()




#Select Handling - DropDown
skillDropDown = driver.find_element_by_xpath(loc.Skills_DD)
selectObject_Skills = Select(skillDropDown)
selectObject_Skills.select_by_value("Backup Management")
time.sleep(1)
selectObject_Skills.select_by_visible_text("Corel Draw")
time.sleep(1)

selectObject_Skills.select_by_index(2)
time.sleep(1)


country_dd = driver.find_element_by_xpath(loc.Country_dropdown)
SelectCountries = Select(country_dd)
SelectCountries.select_by_value("India")
time.sleep(1)
SelectCountries.select_by_index(5)

select_country=driver.find_element_by_xpath(loc.select_country)
select_country.click()
Select_country_serach=driver.find_element_by_xpath(loc.country_search)
Select_country_serach.send_keys("Japan")
Select_country_serach.send_keys(Keys.ENTER)
# driver.find_element_by_xpath(loc.country_india).click()

year_dropdown=driver.find_element_by_id(loc.year_dd)
SelectYears=Select(year_dropdown)
SelectYears.select_by_value("1990")

month_dropdown=driver.find_element_by_xpath(loc.month_dd)
Selectmonth=Select(month_dropdown)
Selectmonth.select_by_index(5)

day_dropdown=driver.find_element_by_id(loc.day_dd)
Selectday=Select(day_dropdown)
Selectday.select_by_value("31")

 # python inbuilt, blind

# scrolling of a web page to bottom
# execute_script - halp to execute the javascript
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

driver.find_element_by_id(loc.pwd).send_keys(td.password)
driver.find_element_by_id(loc.cnf_pwd).send_keys(td.cnf_password)

driver.save_screenshot(r"C:\Users\asisk\PycharmProjects\VariablesDemo\DemoSite_Automation\artifact\screenshots/someScreenshot.png")
time.sleep(3)
driver.find_element_by_xpath(loc.submit).click()

# driver.quit()
# driver.refresh()


# //*[@id="basicBootstrapForm"]/div[5]/div/label[2]/input

# //label[text()=' feMle']

