import constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Auth.auth import Authorization
from ContactUs.contactUs import ContactForm


# WebDrivers configuration using the local storage
# Class Authorization for processing E2E tests for the Auth module functionality
class Main(webdriver.Chrome):
    def __init__(self, driver_path=r"D:\Work\Tools & instruments\Selenium\driver\chromedriver_win32",
                 teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Main, self).__init__(options=options)
        self.implicitly_wait(5)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def apply_registration(self):
        registration = Authorization(driver=self)
        registration.open_login_page()
        webdriver.Chrome.get_screenshot_as_file(self, "media/")
        registration.signup_now_button()
        registration.filling_registration_form(first_name='test', last_name='test', password='1243Qwe!',
                                               description='qweqweqwetest')
        webdriver.Chrome.get_screenshot_as_file(self, "media/")
        registration.filling_login_form()
        webdriver.Chrome.get_screenshot_as_file(self, "media/")
        print("Registration finished")

    def apply_contactus(self):
        contact_form_sending = ContactForm(driver=self)
        contact_form_sending.contact_form_filling(name='test', email='test@test.test',
                                                  contact_number='380999999999', enquiry='qwetest')
        webdriver.Chrome.get_screenshot_as_file(self, "media/")
        print("Contacting process finished")
