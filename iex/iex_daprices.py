from selenium import webdriver
import datetime
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import os
import shutil
import time
import calendar

currentdir = os.path.dirname(__file__)
Initial_path = '/home/kaalachasma/Downloads/iex/'
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_experimental_option("prefs", {                                                                                       
"download.default_directory": f"{Initial_path}",
"download.prompt_for_download": False,
"download.directory_upgrade": True,
"safebrowsing.enabled": True
})


def save_hist_data(year, months):
    def waitUntilDownloadCompleted(maxTime=1200):
        driver.execute_script("window.open()")
        # switch to new tab
        driver.switch_to.window(driver.window_handles[-1])
        # navigate to chrome downloads
        driver.get('chrome://downloads')
        # define the endTime
        endTime = time.time() + maxTime
        while True:
            try:
                # get the download percentage
                downloadPercentage = driver.execute_script(
                    "return document.querySelector('downloads-manager').shadowRoot.querySelector('#downloadsList downloads-item').shadowRoot.querySelector('#progress').value")
                # check if downloadPercentage is 100 (otherwise the script will keep waiting)
                if downloadPercentage == 100:
                    # exit the method once it's completed
                    return downloadPercentage
            except:
                pass
            # wait for 1 second before checking the percentage next time
            time.sleep(1)
            # exit method if the download not completed with in MaxTime.
            if time.time() > endTime:
                break

    starts_on = 1
    for month in months:
        no_month = datetime.datetime.strptime(month, "%b").month
        no_of_days = calendar.monthrange(year, no_month)[1]
        print(f"{no_of_days} days in {month}-{year}")

        driver = webdriver.Chrome(executable_path="/home/kaalachasma/Downloads/chromedriver_linux64/chromedriver.exe", options=chrome_options)
        driver.maximize_window() #For maximizing window
        driver.implicitly_wait(20)
        driver.get("https://www.iexindia.com/marketdata/areaprice.aspx")

        select = Select(driver.find_element_by_name('ctl00$InnerContent$ddlPeriod'))
        select.select_by_visible_text('-Select Range-')

        driver.find_element_by_xpath("//input[@name='ctl00$InnerContent$calFromDate$txt_Date']").click()
        select = Select(driver.find_element_by_xpath("//td[@class='scwHead']/select[@id='scwYears']"))
        select.select_by_visible_text(str(year))
        select = Select(driver.find_element_by_xpath("//td[@class='scwHead']/select[@id='scwMonths']"))
        select.select_by_visible_text(month)

        driver.find_element_by_xpath(f"//td[@class='scwCells' and text()='{starts_on}'] | //td[@class='scwCellsWeekend' and text()='{starts_on}'] | //td[@class='scwInputDate' and text()='{starts_on}']").click()

        # time.sleep(2)
        # test=None
        # while not test:
        #     try:
        #         # driver.find_element_by_xpath(f"//td[@class='scwCells' and contains(text(),'{starts_on}')]").click()
        #         driver.find_element_by_xpath(f"//td[@class='scwCells' and text()='{starts_on}']").click()
        #         # driver.switch_to.frame(driver.find_element_by_xpath(f"//td[@class='scwCells' and text()='{starts_on}']"))
        #         test=True
        #     except IndentationError:
        #         print('Entered from-date except block -IE-1')
        #         # driver.find_element_by_xpath(f"//td[@class='scwCellsWeekend'  and contains(text(), '{starts_on}')]").click()
        #         driver.find_element_by_xpath(f"//td[@class='scwCellsWeekend'  and text()='{starts_on}']").click()
        #         # driver.switch_to.frame(driver.find_element_by_xpath(f"//td[@class='scwCellsWeekend'  and text()='{starts_on}']"))
        #         test=True
        #     except:
        #         print('Entered from-date except block -IE-2')
        #         # driver.find_element_by_xpath(f"//td[@class='scwInputDate'  and contains(text(), '{starts_on}')]").click()
        #         driver.find_element_by_xpath(f"//td[@class='scwInputDate'  and text()='{starts_on}']").click()
        #         # driver.switch_to.frame(driver.find_element_by_xpath(f"//td[@class='scwInputDate'  and text()='{starts_on}']"))
        #         test=True

        driver.switch_to.default_content()
        driver.find_element_by_xpath("//input[@name='ctl00$InnerContent$calToDate$txt_Date']").click()
        select = Select(driver.find_element_by_xpath("//td[@class='scwHead']/select[@id='scwYears']"))
        select.select_by_visible_text(str(year))
        select = Select(driver.find_element_by_xpath("//td[@class='scwHead']/select[@id='scwMonths']"))
        select.select_by_visible_text(month)
        driver.find_element_by_xpath(f"//td[@class='scwCells' and text()='{no_of_days}'] | //td[@class='scwCellsWeekend' and text()='{no_of_days}'] | //td[@class='scwInputDate' and text()='{no_of_days}']").click()
        # time.sleep(2)
        # test=None
        # while not test:
        #     try:
        #         # driver.find_element_by_xpath(f"//td[@class='scwCells'  and contains(text(), '{no_of_days}')]").click()
        #         driver.find_element_by_xpath(f"//td[@class='scwCells' and text()='{no_of_days}']").click()                
        #         test=True
        #     except IndentationError:
        #         print('Entered to-date except block -IE-1')
        #         # driver.find_element_by_xpath(f"//td[@class='scwCellsWeekend'  and contains(text(), '{no_of_days}')]").click()
        #         driver.find_element_by_xpath(f"//td[@class='scwCellsWeekend' and text()='{no_of_days}']").click()
        #         # time.sleep(4)
        #         test=True
        #     except:
        #         print('Entered to-date except block -IE-2')
        #         # driver.find_element_by_xpath(f"//td[@class='scwInputDate'  and contains(text(), '{no_of_days}')]").click()
        #         driver.find_element_by_xpath(f"//td[@class='scwInputDate' and text()='{no_of_days}']").click()
        #         test=True
                
    
        driver.find_element_by_xpath("//input[@name='ctl00$InnerContent$btnUpdateReport']").click()
        driver.find_element_by_xpath("//a[@title='Export drop down menu']").click()
        print("Right before excel button click")
        driver.find_element_by_xpath("//a[@title='Excel']").click()
        waitUntilDownloadCompleted(30)
        print("After the download potentially!")
        
        filename = max([Initial_path + f for f in os.listdir(Initial_path)],key=os.path.getctime)
        shutil.move(filename,os.path.join(Initial_path,f"{month}{year}.xlsx"))

        driver.quit()

def main():

    years = [2012]#list(range(2013,2015))
    months = ['Jan', 'Feb', 'Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    for year in years:
            try:
                save_hist_data(year, months)
            except:
                print("The given month doesn't exist")

if __name__== '__main__':
    main()