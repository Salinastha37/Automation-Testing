import pytest
from utils.driver_setup import driver as create_driver

@pytest.fixture
def driver():
    driver = create_driver()

    yield driver
    driver.quit()
