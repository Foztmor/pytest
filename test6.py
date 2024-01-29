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


def test_avito_login(browser):
    browser.get("https://www.avito.ru")


    login_link = browser.find_element(By.CSS_SELECTOR,"a[data-marker='header/login-button']")
    login_link.click()

    time.sleep(2)

    # Заполняем форму логина и пароля
    username_input = browser.find_element(By.NAME, 'login')
    password_input = browser.find_element(By.NAME, 'password')

    username_input.send_keys("+79080195632")
    password_input.send_keys("bpaz19-01")


    password_input.send_keys(Keys.RETURN)
    time.sleep(3)


    browser.get("https://www.avito.ru/profile")
    time.sleep(2)
    assert 'https://www.avito.ru/profile' in browser.page_source.lower()
