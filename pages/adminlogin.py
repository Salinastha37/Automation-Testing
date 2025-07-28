from selenium.webdriver.common.by import By
from utils.wait_helper import wait_and_find 

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_field = (By.NAME, "email")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")

    def enter_email(self, email): 
        wait_and_find(self.driver, *self.email_field).send_keys(email)

    def enter_password(self, password):
        wait_and_find(self.driver, *self.password_field).send_keys(password)

    def click_login(self):
        wait_and_find(self.driver, *self.login_button).click()

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login() 