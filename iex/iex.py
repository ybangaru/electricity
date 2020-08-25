from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import os
import time
# caps = Selenium::WebDriver::Remote::Capabilities.chrome("chromeOptions" => {"binary" => "Actual Path"})

currentdir = os.path.dirname(__file__)
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_experimental_option("prefs", {                                                                                       
  "download.default_directory": r"/home/kaalachasma/Downloads/iex/",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})
a=1
b=30
years = list(range(2013,2020))
months = ['Jan', 'Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

driver = webdriver.Chrome(executable_path=os.path.join(currentdir, "chromedriver.exe"), options=chrome_options)
driver.get("https://www.iexindia.com/marketdata/areaprice.aspx")
time.sleep(15)

select = Select(driver.find_element_by_name('ctl00$InnerContent$ddlPeriod'))
select.select_by_visible_text('-Select Range-')
time.sleep(4)

driver.find_element_by_xpath("//input[@name='ctl00$InnerContent$calFromDate$txt_Date']").click()
time.sleep(4)
select = Select(driver.find_element_by_xpath("//td[@class='scwHead']/select[@id='scwYears']"))
select.select_by_visible_text(str(years[2]))
time.sleep(4)
select = Select(driver.find_element_by_xpath("//td[@class='scwHead']/select[@id='scwMonths']"))
select.select_by_visible_text(months[3])
time.sleep(4)
# driver.find_element_by_xpath("//td[@class='scwCells' and @id='scwCell_10']").click()
driver.find_element_by_xpath("//td[@class='scwCells'  and contains(text(),'1')]").click()
time.sleep(4)
driver.find_element_by_xpath("//input[@name='ctl00$InnerContent$calToDate$txt_Date']").click()
time.sleep(4)
select = Select(driver.find_element_by_xpath("//td[@class='scwHead']/select[@id='scwYears']"))
select.select_by_visible_text(str(years[2]))
time.sleep(4)
select = Select(driver.find_element_by_xpath("//td[@class='scwHead']/select[@id='scwMonths']"))
select.select_by_visible_text(months[3])
time.sleep(4)
# driver.find_element_by_xpath("//td[@class='scwCells' and @id='scwCell_10']").click()
driver.find_element_by_xpath("//td[@class='scwCells' and contains(text(),'30')]").click()
time.sleep(4)


driver.find_element_by_xpath("//input[@name='ctl00$InnerContent$btnUpdateReport']").click()
time.sleep(15)
driver.find_element_by_xpath("//a[@title='Export drop down menu']").click()
time.sleep(4)
driver.find_element_by_xpath("//a[@title='Excel']").click()
# time.sleep(50)
# driver.quit()
