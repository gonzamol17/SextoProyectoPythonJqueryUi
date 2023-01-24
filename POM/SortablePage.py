import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class SortableLocators:
    listElement = (By.CSS_SELECTOR, "#sortable>li")
    item7Box = (By.CSS_SELECTOR, "#sortable>li:nth-child(7)")


class SortablePage:

    def __init__(self, driver):
        self.driver = driver

    def getListItems(self):
        return self.driver.find_elements(*SortableLocators.listElement)

    def getEachNameItems(self, n):
        return self.driver.find_element(By.CSS_SELECTOR, "#sortable>li:nth-child(" + str(n) + ")").text

    def clickDraggableItem7(self):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(self.driver.find_element(*SortableLocators.item7Box), 0, -100).perform()
