import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_open_avito_and_click_login(browser):
    browser.get("https://www.avito.ru")
    login_link = browser.find_element(By.CSS_SELECTOR, "a[data-marker='header/login-button']")
    login_link.click()
    time.sleep(2)
    assert "login" in browser.current_url