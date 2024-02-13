import constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver


class ContactForm:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    try:
        def contact_form_filling(self, name, email, contact_number, enquiry):

            contact_page = self.driver.find_element(By.XPATH, "//a[@href='https://www.assistancedogs.org.uk/contact"
                                                              "-us/']")
            contact_page.click()

            self.driver.implicitly_wait(5)

            name_field = self.driver.find_element(By.ID, 'input_1_1')
            name_field.send_keys(name)

            email_field = self.driver.find_element(By.ID, 'input_1_5')
            email_field.send_keys(email)

            contact_number_field = self.driver.find_element(By.ID, 'input_1_4')
            contact_number_field.send_keys(contact_number)

            enquiry_field = self.driver.find_element(By.ID, 'input_1_2')
            enquiry_field.send_keys(enquiry)

            submit_button_element = self.driver.find_element(By.ID, 'gform_submit_button_1')
            submit_button_element.click()

    except TimeoutException as e:
        print(f"Ошибка: {e}")
