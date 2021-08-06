import pytest
import sys

@pytest.mark.skip
def test_login():
    print("Login to application")

@pytest.mark.skipif(sys.version_info<(3,9),reason="Python version not supported")
def test_checkout():
    print("Checkout")

@pytest.mark.xfail
def test_logout():
    assert False
    print("Logout from application")


def test_closeApplication():
    assert True
    print("Close the application")