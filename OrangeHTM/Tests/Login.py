
from selenium import webdriver
import unittest
import time
import HtmlTestRunner
import sys
import os 
from selenium.webdriver.common.keys import Keys
# os.environ['PATH'] += r"D:\\New_Start\\FreeCodeCamp"

sys.path.append('D:\\New_Start\\FreeCodeCamp\\OrangeHTM')

from Pages.Login_Page import LoginPage


class OrangeHRM_Tests(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(29)

    def test_01_Login_Logout_validity(self):
        driver = self.driver
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        login = LoginPage(driver)
        login.enter_usename('Admin')
        login.enter_password('admin123')
        login.click_login()
        login.logout()
        # time.sleep(5)

        

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test Complete")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:\\New_Start\\FreeCodeCamp\\Test_Report'))


