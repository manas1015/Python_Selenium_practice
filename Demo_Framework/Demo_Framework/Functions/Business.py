
from Locator import ObjectRepo as OR
from Data import TestData as td
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class BusinessActions:

    def __init__(self):
        print("BUFunctions is initiated")

    def login(self, driver, email_id):
        initialEmailField = driver.find_element_by_id("email")
        initialEmailField.send_keys(td.InitialEmailID)
        goButton = driver.find_element_by_id(OR.SignINButton)
        goButton.click()

    def Name(self,driver,First_Name,Last_Name):
        driver.find_element_by_xpath(OR.First_Name).send_keys(td.First_Name)
        driver.find_element_by_xpath(OR.Last_Name).send_keys(td.Last_Name)

    def Address(self,driver,Emai,Phone,Address,gender,hobbies):
        Email = driver.find_element_by_xpath(OR.Email_Address)
        Email.send_keys(td.Email)
        phone = driver.find_element_by_xpath(OR.Phone).send_keys(td.phone)
        Address = driver.find_element_by_xpath(OR.address)
        Address.send_keys(td.address)

        male = driver.find_element_by_xpath(OR.Male_Radio_Button)
        female = driver.find_element_by_xpath(OR.Female_Radio_Button)
        male.click()
        time.sleep(2)
        if male.is_selected():
            female.click()

        cricket_CB = driver.find_element_by_id(OR.Cricket_Check_Box)
        movies_CB = driver.find_element_by_id(OR.Movies_CB)
        hockey_cb = driver.find_element_by_id(OR.Hockey_CB)

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
            # Selection process
            movies_CB.click()
    def LSCC(self,driver,lang,skill,country,Scountry):
        driver.find_element_by_id(OR.Lang_DropDown).click()

        driver.find_element_by_xpath(OR.Thai_DropDownSelection).click()
        driver.find_element_by_xpath(OR.Swedish_DD_Selection).click()

        time.sleep(1)

        driver.find_element_by_xpath(OR.Thai_CloseButton).click()

        # Select Handling - DropDown
        skillDropDown = driver.find_element_by_xpath(OR.Skills_DD)
        selectObject_Skills = Select(skillDropDown)
        selectObject_Skills.select_by_value("Backup Management")
        time.sleep(1)
        selectObject_Skills.select_by_visible_text("Corel Draw")
        time.sleep(1)

        selectObject_Skills.select_by_index(2)
        time.sleep(1)

        country_dd = driver.find_element_by_xpath(OR.Country_dropdown)
        SelectCountries = Select(country_dd)
        SelectCountries.select_by_value("India")
        time.sleep(1)
        SelectCountries.select_by_index(5)

        select_country = driver.find_element_by_xpath(OR.select_country)
        select_country.click()
        Select_country_serach = driver.find_element_by_xpath(OR.country_search)
        Select_country_serach.send_keys("Japan")
        Select_country_serach.send_keys(Keys.ENTER)
    def DOB(self,driver,year,month,day):
        year_dropdown = driver.find_element_by_id(OR.year_dd)
        selectYears = Select(year_dropdown)
        selectYears.select_by_value("1990")

        month_dropdown = driver.find_element_by_xpath(OR.month_dd)
        Selectmonth = Select(month_dropdown)
        Selectmonth.select_by_index(5)

        day_dropdown = driver.find_element_by_id(OR.day_dd)
        Selectday = Select(day_dropdown)
        Selectday.select_by_value("31")
    def submit(self,driver,pwd,conf_pwd):
        driver.find_element_by_id(OR.pwd).send_keys(td.password)
        driver.find_element_by_id(OR.cnf_pwd).send_keys(td.cnf_password)
        driver.find_element_by_xpath(OR.submit).click()