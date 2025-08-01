from selenium.webdriver.common.by import By
from utils.wait_helper import wait_and_find
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
    
    DASHBOARD_TEXT = (By.XPATH, '//h5[contains(text(), "Samurai Admin")]')
    CREATE_TASK_BTN = (By.XPATH, "//button[contains(text(), 'タスクを作成する')]")
    CREATE_TASK_MODAL_TITLE = (By.XPATH, '//h6[contains(text(), "Create a task")]')
    CLOSE_TASK_BTN = (By.XPATH, '//button[@aria-label="close"]')

    # LOGOUT_BTN = (By.XPATH,"//button[contains(text(), 'ログアウト')]")
    
    #Check if an element is present and visible
    def is_dashboard_loaded(self):
        try:
            wait_and_find(self.driver, *self.DASHBOARD_TEXT)
            WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOGOUT_BTN)
        )
            return True
        except:
            return False
    # def open_create_task_modal(self):
    #     #click create task button and verify modal is visible
    #     create_task_btn = wait_and_find(self.driver, *self.CREATE_TASK_BTN)
    #     create_task_btn.click()
         
    #     # Verify modal title appears
    #     modal_title = wait_and_find(self.driver, *self.CREATE_TASK_MODAL_TITLE)
    #     print("Modal title is:", modal_title.text)
    #     return modal_title.is_displayed()
    # def close_create_task_modal(self):
    #     #Click the close button on the modal and verified it's close
    #     close_btn = wait_and_find(self.driver, *self.CLOSE_TASK_BTN)
    #     close_btn.click()

    #     # Optional: wait until modal disappears
    #     WebDriverWait(self.driver, 5).until(
    #         EC.invisibility_of_element_located(self.CREATE_TASK_MODAL_TITLE)
    #     )
    #     print("Modal closed successfully.")
    #     return True
    
    # def click_logout(self):
    #     logout_btn = wait_and_find(self.driver, *self.LOGOUT_BTN)
    #     logout_btn.click()
    #     print("Logout button clicked successfully")
            
    #     WebDriverWait(self.driver, 5).until(
    #     EC.visibility_of_element_located((By.ID, "email"))  )
    #     print("Logout successful - back to login page.")
 

