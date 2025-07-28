from selenium import webdriver


def driver():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    driver.get("https://ai-samurai.tai.com.np/")

    return driver
   