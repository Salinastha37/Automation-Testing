# pages/message.py
from selenium.webdriver.common.by import By
from utils.wait_helper import wait_and_find

class MessagePage:
    def __init__(self, driver):
        self.driver = driver
        self.subject_input = (By.NAME, "subject")
        self.message_input = (By.NAME, "message")
        self.send_button = (By.XPATH, "//button[contains(text(), 'Send')]")

    def send_message(self, subject, message):
        wait_and_find(self.driver, *self.subject_input).send_keys(subject)
        wait_and_find(self.driver, *self.message_input).send_keys(message)
        wait_and_find(self.driver, *self.send_button).click()
