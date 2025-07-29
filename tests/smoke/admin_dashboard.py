

import pytest
from selenium.webdriver.common.by import By
from pages.adminlogin import LoginPage
from pages.admindashboard import DashboardPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_dashboard_elements(driver):
    # Step 1: Login
    login = LoginPage(driver)
    login.login("admin@tai.com.np", "admin123")  

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//h5[contains(text(), "Samurai Admin")]'))
    )

    print(" Current URL:", driver.current_url)
    # Step 2: Dashboard assertions
    dashboard = DashboardPage(driver)

    # Assert Dashboard text
    assert dashboard.is_dashboard_loaded()
    #  Click buttons
    dashboard.click_create_task()
    print(" Clicked Create Task")

    # dashboard.click_close_task()
    # print(" Clicked Close Task")

    # dashboard.click_logout()
    # print(" Clicked logout") 

    #  Click buttons
    

    # dashboard.click_schedule_interview()
    # print(" Clicked Schedule Interview")

    # dashboard.click_create_appointment()
    # print("Clicked Create Appointment")
