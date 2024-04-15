import time
import pytest
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
from Utils import utils as utils

from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from POM.Dialog import DialogPage


class TestDialog(BaseClass):

    def test_Dialog(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.clickDialogLink()
        driver.execute_script("window.scrollTo(0, 200)")
        time.sleep(1)
        driver.switch_to.frame(0)
        time.sleep(1)
        dp = DialogPage(driver)
        assert "default dialog which" in dp.readTextFromPopUp()
        dp.clickCloseOption()
        driver.switch_to_default_content()
        time.sleep(2)
        dp.selectModalForm()
        time.sleep(2)
        driver.switch_to.frame(0)
        dp.selectBtnCreateNewUser()
        assert "Create new user" == dp.getTitleFromModal()
        dp.selectCreateAccount()
        time.sleep(2)
        users = dp.getAllUsers()
        for user in users:
            time.sleep(2)
            if user.text == "Jane Smith":
                print("La usuaria " + user.text + " ha sido creada con éxito")
                break
            print("\nUsuario/a ya existente: " + user.text)
        time.sleep(2)

