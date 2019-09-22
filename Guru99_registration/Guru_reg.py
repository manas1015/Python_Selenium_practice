from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import Gur_locator as gl
import Guru_data as gd

driver=webdriver.Chrome(gl.DriverPATH)
App_title=driver.get(gl.AppURL)
driver.maximize_window()
driver.implicitly_wait(10)
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

Title=driver.find_element_by_xpath(gl.title)
Title_dd=Select(Title)
Title_dd.select_by_value("Captain")
time.sleep(1)
Title_dd.select_by_visible_text("Miss")

Fname=driver.find_element_by_xpath(gl.F_name)
Fname.send_keys(gd.First_Name)
Sname=driver.find_element_by_xpath(gl.S_name)
Sname.send_keys(gd.Last_Name)
Phone=driver.find_element_by_xpath(gl.Phone)
Phone.send_keys(gd.phone)

D_yr=driver.find_element_by_xpath(gl.DOB_yr)
Y_dd=Select(D_yr)
Y_dd.select_by_value("1988")

D_mm=driver.find_element_by_xpath(gl.DOB_Mnth)
M_dd=Select(D_mm)
M_dd.select_by_visible_text("July")

D_day=driver.find_element_by_xpath(gl.DOB_dy)
D_dd=Select(D_day)
D_dd.select_by_value("11")

full=driver.find_element_by_xpath(gl.Full)
provisional=driver.find_element_by_xpath(gl.Provisional)
if full.is_selected():
    provisional.click()
# reset=driver.find_element_by_xpath(gl.reset)
# reset.click()

licence_P=driver.find_element_by_id(gl.Licence_period)
L_dd=Select(licence_P)
L_dd.select_by_index(5)

occu=driver.find_element_by_id(gl.occupation)
occu_dd=Select(occu)
occu_dd.select_by_value("11")
time.sleep(3)
# driver.execute_script("window.scrollTo(0,-500)")

# AD_str=driver.find_element_by_id(gl.ad_street)
# AD_str.send_keys(gd.street)
# AD_city=driver.find_element_by_id(gl.ad_city)
# AD_city.send_keys(gd.city)
# AD_pcode=driver.find_element_by_id(gl.ad_post)
# AD_pcode.send_keys(gd.postcode)
# Email=driver.find_element_by_id(gl.Email)
# driver.execute_script("arguments[0].scrollIntoViews;",Email)
# Email.send_keys(gd.email)

pwd=driver.find_element_by_id(gl.pwd)
pwd.send_keys(gd.password)
cnf_pwd=driver.find_element_by_id(gl.cnf_pwd)
cnf_pwd.send_keys(gd.cnf_pwd)

submit=driver.find_element_by_xpath(gl.submit)
submit.click()


