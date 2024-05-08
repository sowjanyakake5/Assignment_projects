# test_login_page.py

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from LoginPage import LoginPage

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def login_page(driver):
    driver.get("https://www.linkedin.com/")
    return LoginPage(driver)

def test_verify_login(driver, login_page):
    login_page.enter_email("kanike100@gmail.com")
    login_page.enter_password("pppppppppwd21234%")
    login_page.click_sign_in_button()

    # assertion to verify successful login
    assert "Feed" in driver.title

def test_verify_view_profile_click(driver, login_page):
    login_page.click_on_user_name_arrow_sign()
    login_page.click_on_view_profile()

    # assertion to verify profile view page
    assert "Profile" in driver.title
