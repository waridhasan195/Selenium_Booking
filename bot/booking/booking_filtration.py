from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BookingFiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver
    
    def apply_star_ratting(self, *star_values):
        star_filtration_box = self.driver.find_element(By.ID, 'filter_group_class_:R1cq:')
        star_child_elements = star_filtration_box.find_elements(By.CSS_SELECTOR, '*')

        for star_value in star_values:
            for star_element in star_child_elements:
                if str(star_element.get_attribute('innerHTML')).strip() == f'{star_value} stars':
                    star_element.click()
                    print("Star Clicked.")


    def sort_price_lowest_first(self):
        element = self.driver.find_element(
            By.CSS_SELECTOR, 'button[data-testid="sorters-dropdown-trigger"]'
        )
        element.click()

        element2 = self.driver.find_element(
            By.CSS_SELECTOR, 'button[data-id="price"]'
        )
        element2.click()
        print("Price Sorting Clicked.")
    
