from pages.adminlogin import LoginPage
from utils.wait_helper import wait_and_find
from selenium.webdriver.common.by import By


def test_admin_login_success(driver):
    driver.get("https://ai-samurai.tai.com.np/admin/login") 
    login = LoginPage(driver)
    login.login("admin@tai.com.np", "admin123")     

    #Wait for dashboard element after login
    dashboard_heading = wait_and_find(driver, By.XPATH, '//h5[contains(text(), "Samurai Admin")]', timeout=3)
     # Assert element is visible
    assert dashboard_heading.is_displayed(), "Dashboard heading not visible"

    # Assert URL contains '/admin'
    assert "/admin" in driver.current_url, f"Expected URL to contain '/admin', but got: {driver.current_url}"


    assert "Samurai Admin" in driver.title or "/admin" in driver.current_url
