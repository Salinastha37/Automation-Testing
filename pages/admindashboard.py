from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.wait_helper import wait_and_find

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    DASHBOARD_TEXT = (By.XPATH, '//h5[contains(text(), "Samurai Admin")]')
    CREATE_TASK_BTN = (By.XPATH, "//button[contains(text(), 'タスクを作成する')]")
    CLOSE_TASK_BTN =(By.XPATH, '//button[@aria-label="close"]')

    LOGOUT_BTN = (By.XPATH,"//button[contains(text(), 'ログアウト')]")
   

    def is_dashboard_loaded(self):
        return self.driver.find_element(*self.DASHBOARD_TEXT).is_displayed()
    def click_create_task(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.CREATE_TASK_BTN)
        ).click()

        modal_title = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//h6[contains(text(), "Create a task")]'))
        )
        print("Modal title is:", modal_title.text)

        try:
            WebDriverWait(self.driver, 5).until(
                EC.invisibility_of_element_located((By.CLASS_NAME, "MuiBackdrop-root"))
            )
        except:
            print("No backdrop or already invisible.")

        close_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CLOSE_TASK_BTN)
        )
        print("Close button text is:", close_btn.text)
        close_btn.click()

    # def click_close_task(self):
    #     WebDriverWait(self.driver, 5).until(
    #         EC.visibility_of_element_located((By.CLASS_NAME, "MuiButton-root"))  # or adjust the modal class
    #     )
    #     WebDriverWait(self.driver, 5).until(
    #         EC.element_to_be_clickable(self.CLOSE_TASK_BTN)
    #     ).click()

    # def click_logout(self):
    #      wait_and_find(self.driver, *self.LOGOUT_BTN).click()

    
    
   
    

    # def click_schedule_interview(self):
    #     self.driver.find_element(*self.SCHEDULE_INTERVIEW_BTN).click()

    # def click_create_appointment(self):
    #     self.driver.find_element(*self.CREATE_APPOINTMENT_BTN).click()
    

