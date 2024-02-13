import constants as const
import os
import random
import string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from ContactUs.contactUs import ContactForm


# WebDrivers configuration using the local storage
# Class Authorization for processing E2E tests for the Auth module functionality


class Authorization:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.auth_data_storage_email = {}  # Storage for auth data storing for different functions using
        self.auth_data_storage_password = {}
    # Clicking on the "Login" button to redirect to the "Login" page
    def open_login_page(self):
        try:
            login_button = self.driver.find_element(By.XPATH,
                                                    "//a[@class='nav-link'][@href='https://www.assistancedogs.org.uk/log-in/']")
            login_button.click()
        except TimeoutException as e:
            print(f"Error: Timeout Open Login Page: {e}")

    # Clicking on the "SignUp" button to redirect to the "Sign_Up" page
    def signup_now_button(self):
        try:
            login_button = self.driver.find_element(By.XPATH,
                                                    "//a[@href='https://www.assistancedogs.org.uk/register/']")
            login_button.click()
        except TimeoutException as e:
            print(f"Error: Timeout Signup Button: {e}")

    def generate_random_email(self, length=10):
        """Генерирует случайный адрес электронной почты"""
        letters_and_digits = string.ascii_letters + string.digits
        email = ''.join(random.choice(letters_and_digits) for _ in range(length)) + "@test.com"
        return email

    # Here we are filling the registration form and completing the auth process
    def filling_registration_form(self, first_name, last_name, password, description):
            try:
                first_name_field = self.driver.find_element(By.ID, 'user_firstname')
                first_name_field.send_keys(first_name)

                last_name_field = self.driver.find_element(By.ID, 'user_lastname')
                last_name_field.send_keys(last_name)

                email = self.generate_random_email()
                self.auth_data_storage_email['email'] = email
                email_field = self.driver.find_element(By.ID, 'user_email')
                email_field.send_keys(email)

                self.auth_data_storage_password['password'] = password
                password_field = self.driver.find_element(By.ID, 'user_password')
                password_field.send_keys(password)

                description_field = self.driver.find_element(By.ID, 'user_description')
                description_field.send_keys(description)

                privacy_policy_checkbox = self.driver.find_element(By.ID, 'privacy')
                privacy_policy_checkbox.click()

                register_button = self.driver.find_element(By.NAME, 'submit_registration')
                register_button.click()

            except TimeoutException as e:
                print(f"Auth Timeout Error: {e}")

    # This is the place for the Login functionality
    def filling_login_form(self):
        try:
            login_page_navigation = self.driver.find_element(By.XPATH,
                    "//a[@class='nav-link'][@href='https://www.assistancedogs.org.uk/log-in/']")
            login_page_navigation.click()

            email_field = self.driver.find_element(By.ID, 'username')
            email_field.send_keys(self.auth_data_storage_email.get('email'))

            password_from_storage = self.auth_data_storage_password.get('password')
            password_field = self.driver.find_element(By.ID, 'password')
            password_field.send_keys(password_from_storage)

            remember_me_checkbox = self.driver.find_element(By.ID, 'remember')
            remember_me_checkbox.click()

            submit_button = self.driver.find_element(By.NAME, 'submit_login')
            submit_button.click()
        except TimeoutException as e:
            print(f"login Timeout Error: {e}")
# This is the place for the Forgot Password functionality, I will finish this bellow soon
