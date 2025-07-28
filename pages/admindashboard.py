
from selenium.webdriver.common.by import By
from utils.wait_helper import wait_and_find
# from pages.adminlogin import LoginPage
class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    DASHBOARD_TEXT = (By.XPATH, '//h5[contains(text(), "Samurai Admin")]')
    CREATE_TASK_BTN = (By.XPATH, "//button[contains(text(), 'タスクを作成する')]")
    CLOSE_TASK_BTN =(By.XPATH, "//svg[contains(@class, 'MuiSvgIcon-root')]")
    # SCHEDULE_INTERVIEW_BTN = (By.XPATH, "//button[contains(text(), 'インタビューを予約する')]")
    # CREATE_APPOINTMENT_BTN = (By.XPATH, "//button[contains(text(), 'アポイントメントの作成')]")

    def is_dashboard_loaded(self):
        return self.driver.find_element(*self.DASHBOARD_TEXT).is_displayed()

    

    def click_create_task(self):
        self.driver.find_element(*self.CREATE_TASK_BTN).click()
    
    def click_close_task(self):
        self.driver.find_element(*self.CLOSE_TASK_BTN).click()
    

    # def click_schedule_interview(self):
    #     self.driver.find_element(*self.SCHEDULE_INTERVIEW_BTN).click()

    # def click_create_appointment(self):
    #     self.driver.find_element(*self.CREATE_APPOINTMENT_BTN).click()
    

