import booking.constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from booking.booking_filtration import BookingFiltration
from booking.booking_report import BookingReport
from prettytable import PrettyTable


class Booking(webdriver.Chrome):
    def __init__(self, driver_path = r"D:/New_Start/FreeCodeCamp/Driver/chromedriver_win32/chromedriver.exe", teardown = False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Booking, self).__init__(options=options)
        self.implicitly_wait(40)
        self.maximize_window()

    def __exit__(self, exc_type, exc, traceback):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

        try:
            print("Add Contains.")
            adds = self.find_element('XPATH', '//*[@id="close"]')
            adds.click()
            print("Clicked")
        except:
            print("No Adds.....")

    def change_currency(self, currency = None):
        time.sleep(5)
        currency_element = self.find_element(
            By.CSS_SELECTOR, 'button[data-tooltip-text="Choose your currency"]'
            )
        currency_element.click()

        selected_currency_element = self.find_element(
            By.CSS_SELECTOR, f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
            )
        selected_currency_element.click()
        print("Currency Change Complete")


    def selecet_place_to_go(self, place_to_go):
        search_field = self.find_element(
            By.ID, 'ss'
        )
        search_field.clear()
        search_field.send_keys(place_to_go)

        first_result = self.find_element(
            By.CSS_SELECTOR, 'li[data-i="0"]'
        )
        first_result.click()
        print("Search Complete")


    def select_date(self, check_in_date, Check_out_date):
        check_in_date = self.find_element(
            By.CSS_SELECTOR, f'td[data-date="{check_in_date}"]'
        )
        check_in_date.click()
        print("Check in Complete")

        Check_out_date = self.find_element(
            By.CSS_SELECTOR, f'td[data-date="{Check_out_date}"]'
        )
        Check_out_date.click()
        print("Check Out Complete")
        # time.sleep(5)

    
    def select_adults(self, count =1):
        selection_element = self.find_element(
            By.ID, 'xp__guests__toggle'
        )
        selection_element.click()

        while True:
            decrease_adult_element = self.find_element(
                By.CSS_SELECTOR, 'button[aria-label="Decrease number of Adults"]'
            )
            decrease_adult_element.click()

            adults_value_element = self.find_element(
                By.ID, 'group_adults'
            )
            adults_value = adults_value_element.get_attribute('value')

            if int(adults_value) ==1:
                print("Break . . . ")
                break
        
        inclease_button_element = self.find_element(
            By.CSS_SELECTOR, 'button[aria-label="Increase number of Adults"]'
        )

        for _ in range(count - 1):
            inclease_button_element.click()
        print("Adults Inclease Complete.")


    def click_search(self):
        search_button = self.find_element(
            By.CSS_SELECTOR, 'button[type="submit"]'
        )
        search_button.click()
        print("Search Comlete.")
    

    def apply_filtration(self):
        filtration = BookingFiltration(driver = self)
        filtration.apply_star_ratting(3, 4, 5)
        filtration.sort_price_lowest_first()
    

    def report_results(self):
        hotel_boxes = self.find_element(
            By.CLASS_NAME, 'd4924c9e74'
            )
        # .find_elements(By.CLASS_NAME, 'a826ba81c4')

        report = BookingReport(hotel_boxes)
        table = PrettyTable(
            field_names= ["Hotel Name", "Hotel Price", "Hotel Score"]
        )
        table.add_rows(report.pull_deal_box_attributes())
        print(table)
        

        # print(report.pull_deal_box_attributes())
        
        # report.display_table()
        







    





