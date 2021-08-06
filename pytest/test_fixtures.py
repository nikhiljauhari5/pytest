'''
    PreCondition
        Setup, Connection,API

    Test

    Test

    Assertion

    PostCondition
        clean,close,close

'''



import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver=None
@pytest.fixture
def setup():
    print("Start Browser")
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    driver.quit()
    print("Close Browser")


def test_1(setup):
    driver.get("https://www.google.com/")
    print("Test 1 Executed")

def test_2(setup):
    driver.get("https://www.facebook.com/")
    print("Test 2 Executed")

def test_3(setup):
    driver.get("https://www.gmail.com/")
    print("Test 3 Executed")
