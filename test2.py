import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_avito_search_result_displayed(browser):
    browser.get("https://www.avito.ru")
    search_box = browser.find_element(By.CSS_SELECTOR, 'input[class="input-input-Zpzc1"]')
    search_box.send_keys("бетономешалка" + Keys.RETURN)
    time.sleep(2)
    search_results = browser.find_element(By.CSS_SELECTOR, "div[itemtype='http://schema.org/BreadcrumbList']")
    assert search_results.is_displayed()