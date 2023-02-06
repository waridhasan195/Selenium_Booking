
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import collections

class BookingReport:
    def __init__(self, box_section_element:WebElement):
        self.box_section_element = box_section_element
        self.deal_boxes = self.pull_deal_boxes()
        print(self.box_section_element)



    def pull_deal_boxes(self):
        return self.box_section_element.find_elements(
            By.CLASS_NAME, 'a826ba81c4'
        )


    
    def pull_deal_box_attributes(self):
        collection = []
        for deal_box in self.deal_boxes:
            hotel_name = deal_box.find_element(
                By.CLASS_NAME, 'fcab3ed991'
            ).get_attribute('innerHTML').strip()

            hotel_price = deal_box.find_element(
                By.CLASS_NAME, 'e729ed5ab6"'
            ).get_attribute('innerHTML').strip()

            hotel_score = deal_box.find_element(
                By.CLASS_NAME, 'b5cd09854e'
            ).get_attribute('innerHTML').strip()


            collection.append(
                [hotel_name, hotel_price, hotel_score]
            )
        return collection


            

            



