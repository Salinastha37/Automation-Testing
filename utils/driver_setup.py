from selenium import webdriver


def driver():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)

    return driver
   