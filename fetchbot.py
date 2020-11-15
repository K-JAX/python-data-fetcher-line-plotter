import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

dir_path = os.path.dirname(os.path.realpath(__file__))
data_dir = dir_path + '/Datasets/'

class FetchBot:
	def __init__(self):
		# set profile
		profile = webdriver.FirefoxProfile()
		profile.set_preference("browser.download.folderList", 2)
		profile.set_preference("browser.altClickSave", True)
		profile.set_preference("browser.download.manager.showWhenStarting", False)
		profile.set_preference("browser.download.dir", data_dir)
		profile.set_preference("browser.download.panel.shown", False)
		profile.set_preference("browser.helperApps.neverAsk.openFile","application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;application/xls;text/csv")
		profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;application/xls;text/csv")

		driver = webdriver.Firefox(firefox_profile=profile)


		driver.get('https://data.bls.gov/cgi-bin/surveymost?ln')

		ulDD = driver.find_element_by_xpath("//*[contains(text(), 'Unemployment Level -')]")
		ulInput = ulDD.find_element_by_css_selector('input')
		ulInput.click()

		loadDataSub = driver.find_element_by_css_selector('input[type="Submit"]')
		loadDataSub.click()
		sleep(1)

		# data page
		selectCurrentFromDropdown = driver.find_element_by_xpath('//select[@name="from_year"]/option[text()="2020"]')
		selectCurrentFromDropdown.click()

		updateDateButton = driver.find_element_by_xpath('//input[@name="Go"]').click()

		downloadClick = driver.find_element_by_xpath('//input[@id="download_xlsx"]').click()


