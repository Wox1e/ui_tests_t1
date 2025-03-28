"""Модуль с фикстурами для pytest"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="session")
def driver_setup():
    """Инициализация вебдрайвера для Chrome"""
    service = Service(executable_path="./drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.set_page_load_timeout(5)
    yield driver
    driver.quit()
