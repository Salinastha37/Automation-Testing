from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver



def create_driver(browser="firefox"):
   
    if browser == "firefox":
        options = webdriver.FirefoxOptions()
        # options.add_argument("--headless")  # Uncomment if headless needed
        return webdriver.Firefox(options=options)

    elif browser == "chrome":
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")  # Uncomment if headless needed
        return webdriver.Chrome(options=options)

    else:
        raise ValueError("Unsupported browser: {}".format(browser))


def wait_and_find(driver, by, value, timeout=30):

    
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((by, value))
    )

