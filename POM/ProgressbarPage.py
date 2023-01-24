import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class ProgressbarLocators:
    btnStartDownload = (By.CSS_SELECTOR, "#downloadButton")
    getStatusDownload = (By.CSS_SELECTOR, "#dialog>div.progress-label")
    btnCloseDownload = (By.CSS_SELECTOR, "body div.ui-helper-clearfix>div")
    selectModalOption = (By.CSS_SELECTOR, "#content ul>li:nth-child(3)>a")


class ProgressbarPage:

    def __init__(self, driver):
        self.driver = driver

    def selectBtnStartDownload(self):
        self.driver.find_element(*ProgressbarLocators.btnStartDownload).click()

    def getCurrentStatus(self):
        return self.driver.find_element(*ProgressbarLocators.getStatusDownload).text

    def closePopUpDownload(self):
        self.driver.find_element(*ProgressbarLocators.btnCloseDownload).click()

    def selectModalOption(self):
        self.driver.find_element(*ProgressbarLocators.selectModalOption).click()
