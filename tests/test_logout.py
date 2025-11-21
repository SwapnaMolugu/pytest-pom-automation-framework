from pages.logout import LogoutPage

def test_logout(driver, login):

   # Assert login was successful
    logout = LogoutPage(driver)
    assert logout is not None, "Login failed - Logout option not found."