import time
import pytest
import unittest
import sys
import os

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
from Utils import utils as utils

from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from POM.SortablePage import SortablePage


class TestSortable(BaseClass):

    def test_Sortable(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.clickSortableLink()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 200)")
        driver.switch_to.frame(0)
        sp = SortablePage(driver)
        cant = len(sp.getListItems())
        print("La cantidad de items listados es: " + str(cant))
        aux = sp.getListItems()
        n = 1
        for i in aux:
            print(sp.getEachNameItems(n))
            n = n+1
        time.sleep(2)
        sp.clickDraggableItem7()
        time.sleep(2)
        n = 1
        nas = 1
        print("\nY ahora, habiendo movido el item 7, la lista a quedado de la siguiente manera:")
        for i in aux:
            print(sp.getEachNameItems(n))
            if nas == 5:
                assert sp.getEachNameItems(n) == "Item 7"
                print("En la posición 5, está el item 7, como es lo esperado")
            n = n + 1
            nas = nas+1




