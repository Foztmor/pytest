import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_avito_all_categories_button(browser):
    browser.get("https://www.avito.ru")

    # Находим кнопку "Все категории" и кликаем по ней
    all_categories_button = browser.find_element(By.CSS_SELECTOR, "button[data-marker='top-rubricator/all-categories']")
    all_categories_button.click()
    time.sleep(2)  # Подождем, чтобы страница успела загрузиться

    # Проверяем, что переход успешно произошел и мы находимся на странице с категориями
    rubricator_wrapper = browser.find_element(By.CLASS_NAME, "new-rubricator-content-root_wrapper-tPzn5")
    assert rubricator_wrapper.is_displayed()