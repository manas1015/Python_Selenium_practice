from selenium import  webdriver
# from selenium.webdriver.common.keys import keys as keyBoard
import time
from selenium.webdriver.chrome.options import Options

option = Options()
option.headless = False
driver = webdriver.Chrome( r'F:\Py browser engine\chromedriver_win32\chromedriver.exe',options=option)
driver.get("https://www.snapdeal.com/search?keyword=football&santizedKeyword=&catId=&categoryId=0&suggested=false&vertical=&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy")
driver.maximize_window()
print("Only when parent window is available "+ driver.current_window_handle)

driver.find_element_by_xpath("(//img[@class='product-image '])[1]").click()

print("After opening the child window"+str(driver.window_handles))
idsOfWindow = driver.window_handles
driver.switch_to.window(idsOfWindow[1])

driver.find_element_by_xpath("//span[@class='intialtext' and text()='add to cart']").click()

driver.switch_to.window(idsOfWindow[0])

driver.find_element_by_xpath("//*[@id='view-more-parent-cat']").click()