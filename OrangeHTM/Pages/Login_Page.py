
import sys

sys.path.append('D:\\New_Start\\FreeCodeCamp\\OrangeHTM')

from Locators.locators import locators

class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.login_username_textbox_name = locators.login_username_textbox_name
        self.login_password_passwordbox_name = locators.login_password_passwordbox_name
        self.login_button_XPath = locators.login_button_XPath
        self.frofile_XPath = locators.profile_XPath
        self.logout_XPath = locators.logout_button_XPath

    def enter_usename(self, username):
        self.driver.find_element('name', self.login_username_textbox_name).clear()
        self.driver.find_element('name', self.login_username_textbox_name).send_keys(username)
    
    def enter_password(self, password):
        self.driver.find_element('name', self.login_password_passwordbox_name).clear()
        self.driver.find_element('name', self.login_password_passwordbox_name).send_keys(password)

    def click_login(self):
        self.driver.find_element('xpath', self.login_button_XPath).click()

    def logout(self):
        self.driver.find_element('xpath', self.frofile_XPath).click()
        self.driver.find_element('xpath', self.logout_XPath).click()



