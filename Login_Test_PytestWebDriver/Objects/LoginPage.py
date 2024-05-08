# LoginPage.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        self.email_text = (By.XPATH, "//input[@name='session_key']")
        self.password_text = (By.XPATH, "//input[@name='session_password']")
        self.sign_in_btn = (By.XPATH, "//button[@type='submit']")
        self.arrow_sign = (By.XPATH, "//button[@id='ember18']")
        self.view_profile_text = (By.XPATH, "//div[@id='ember20']")

    def enter_email(self, email_string):
        email_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.email_text))
        email_input.clear()
        email_input.send_keys(email_string)

    def enter_password(self, password_string):
        password_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.password_text))
        password_input.clear()
        password_input.send_keys(password_string)

    def click_sign_in_button(self):
        sign_in_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.sign_in_btn))
        sign_in_button.click()

    def click_on_user_name_arrow_sign(self):
        arrow_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.arrow_sign))
        arrow_button.click()

    def click_on_view_profile(self):
        view_profile_link = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.view_profile_text))
        view_profile_link.click()
