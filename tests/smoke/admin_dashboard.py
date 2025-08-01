from pages.admindashboard import DashboardPage
from pages.adminlogin import LoginPage

def test_dashboard(driver):
     #step1:Login 
    login = LoginPage(driver)
    login.login("admin@tai.com.np", "admin123")

    #step2: Verify dashboard loaded
    dashboard = DashboardPage(driver)
    assert dashboard.is_dashboard_loaded(), "Dashboard did not load properly."

    print("Dashboard loaded successfully.")

#     # step3:Open create task modal and verify it's visible
#     assert dashboard.open_create_task_modal(), "Create Task modal did not appear"
#     print("Modal opened")

#     #step4:Close the modal and verify it's closed
#     assert dashboard.close_create_task_modal(), "Modal did not close"
#     print("Modal closed")
    
    # # step3: logout 
    # dashboard.click_logout()
    