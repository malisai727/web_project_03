import pytest
from selenium import webdriver
from TestDatas.common_datas import login_url


@pytest.fixture
def init_driver():
    driver = webdriver.Chrome()
    driver.get(login_url)
    driver.maximize_window()
    yield driver
    driver.quit()