import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture(scope='module')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_add_to_favorites(browser):
    browser.get("https://www.avito.ru")


    login_link = browser.find_element(By.CSS_SELECTOR, "a[data-marker='header/login-button']")
    login_link.click()

    time.sleep(2)


    username_input = browser.find_element(By.NAME, 'login')
    password_input = browser.find_element(By.NAME, 'password')

    username_input.send_keys("+79080195632")
    password_input.send_keys("bpaz19-01")


    password_input.send_keys(Keys.RETURN)
    time.sleep(3)


    first_ad = browser.find_element(By.CLASS_NAME, "photo-slider-image-YqMGj")
    current_window_handle = browser.current_window_handle
    first_ad.click()

    time.sleep(4)


    all_handles = browser.window_handles
    new_window_handle = [handle for handle in all_handles if handle != current_window_handle][0]
    browser.switch_to.window(new_window_handle)


    add_to_favorites_button = browser.find_element(By.XPATH, "//button[@data-marker='item-view/favorite-button' and @class='desktop-1l3k1vq']")
    add_to_favorites_button.click()


    time.sleep(3)

    favorite_ads = browser.find_element(By.CLASS_NAME, "desktop-1l3k1vq")
    assert favorite_ads.is_displayed(), "Объявление не добавлено в избранное"