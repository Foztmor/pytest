import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_avito_logo_redirects_to_homepage(browser):
    browser.get("https://www.avito.ru")
    # Находим логотип и кликаем по нему
    logo = browser.find_element(By.CSS_SELECTOR, "a[data-marker='search-form/logo']")
    logo.click()
    time.sleep(2)  # Позволим странице загрузиться
    # Проверяем, что URL соответствует главной странице
    assert browser.current_url == "https://www.avito.ru/"