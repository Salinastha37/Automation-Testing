# tests/smoke/admin_send_message.py
from pages.adminlogin import LoginPage
from pages.admindashboard import DashboardPage
from pages.adminmessage import MessagePage

def test_admin_send_message(driver):
    driver.get("https://ai-samurai.tai.com.np/admin/login")

    # Login
    login = LoginPage(driver)
    login.login("admin@tai.com.np", "admin123")

    # Navigate to Message section
    dashboard = DashboardPage(driver)
    dashboard.go_to_message_page()

    # Send a message
    message_page = MessagePage(driver)
    message_page.send_message("Test Subject", "This is an automated test message.")
