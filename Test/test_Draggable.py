import time
import pytest
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
import HtmlTestRunner
from Utils import utils as utils

from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from POM.DraggablePage import DraggablePage


@pytest.mark.usefixtures("test_setup")
class TestDraggable(BaseClass):

    def test_Draggable(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.clickDraggableLink()
        time.sleep(2)
        driver.switch_to.frame(0)
        time.sleep(2)
        dp = DraggablePage(driver)
        dp.clickDraggable()
        time.sleep(2)
