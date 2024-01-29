import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_avito_search(browser):
    browser.get("https://www.avito.ru")

    search_input = browser.find_element(By.CSS_SELECTOR,'input[class="input-input-Zpzc1"]')
    search_input.send_keys("iphone" + Keys.RETURN)
    time.sleep(2)

                                         
    item_links = browser.find_elements("xpath", "//div[@data-marker='item']")
    if item_links:
        item_links[0].click()
        time.sleep(2)
        assert "iphone" in browser.title.lower()
 
