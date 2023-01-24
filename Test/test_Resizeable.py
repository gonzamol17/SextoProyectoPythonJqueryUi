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
from POM.ResizeablePage import ResizeablePage


@pytest.mark.usefixtures("test_setup")
class TestResizeable(BaseClass):

    def test_Resizeable(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.clickResizeableLink()
        driver.execute_script("window.scrollTo(0, 300)")
        time.sleep(2)
        driver.switch_to.frame(0)
        time.sleep(2)
        rp = ResizeablePage(driver)
        rp.clickResizeable()
        time.sleep(2)

