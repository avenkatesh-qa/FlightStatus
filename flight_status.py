import time

from selenium import webdriver
from selenium.webdriver.common.by import By

DATE = "Monday, Apr 15"
CITIES = ["Bangalore", "Delhi", "Goa", "Chandigarh", "Hyderabad", "Nagpur", "Dubai"]

data_rows_xpath = "//tbody/tr[contains(@class,'hidden-xs') and @data-date='%s']" % DATE



driver = webdriver.Chrome()

driver.get("https://www.flightradar24.com/data/airports/pnq")
driver.maximize_window()

# accept cookies popup
try:
    alert = driver.switch_to.alert
    alert.accept()
except:
    pass

arrivals_tab = driver.find_element(By.PARTIAL_LINK_TEXT, "arrivals")
arrivals_tab.click()
time.sleep(5)

elements = driver.find_elements(By.XPATH, data_rows_xpath)
n = len(elements)
for i in range(1,n+1):
    td_elements = driver.find_elements(By.XPATH, "//tbody/tr[contains(@class,'hidden-xs') and @data-date='%s'][%d]/td//span"%(DATE,i))
    city = td_elements[1].text
    if city in CITIES:
        status = td_elements[4].text
        print("%s: %s"%(city,status))

driver.quit()