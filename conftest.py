import pytest
from utils.driver_setup import driver 

@pytest.fixture
def driver():
    driver = driver(browser="firefox")
    yield driver
    driver.quit()
